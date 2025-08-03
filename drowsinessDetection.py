import cv2
import mediapipe as mp
import numpy as np
from math import hypot

# Initialize MediaPipe Face Mesh
mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(static_image_mode=False, max_num_faces=1, refine_landmarks=True)
mp_drawing = mp.solutions.drawing_utils

# Eye landmark indices for both eyes (from MediaPipe's 468 landmarks)
LEFT_EYE = [362, 385, 387, 263, 373, 380]  # outer and inner eye
RIGHT_EYE = [33, 160, 158, 133, 153, 144]

# Function to calculate blinking ratio
def get_blinking_ratio(eye_points, landmarks, image_w, image_h):
    p1 = landmarks[eye_points[0]]
    p2 = landmarks[eye_points[3]]
    p3 = landmarks[eye_points[1]]
    p4 = landmarks[eye_points[2]]
    p5 = landmarks[eye_points[5]]
    p6 = landmarks[eye_points[4]]

    left_point = int(p1.x * image_w), int(p1.y * image_h)
    right_point = int(p2.x * image_w), int(p2.y * image_h)
    top_center = midpoint(int(p3.x * image_w), int(p3.y * image_h), int(p4.x * image_w), int(p4.y * image_h))
    bottom_center = midpoint(int(p5.x * image_w), int(p5.y * image_h), int(p6.x * image_w), int(p6.y * image_h))

    hor_line_length = hypot(right_point[0] - left_point[0], right_point[1] - left_point[1])
    ver_line_length = hypot(top_center[0] - bottom_center[0], top_center[1] - bottom_center[1])
    
    ratio = hor_line_length / ver_line_length if ver_line_length != 0 else 0
    return ratio

# Helper function to find midpoint
def midpoint(x1, y1, x2, y2):
    return int((x1 + x2)/2), int((y1 + y2)/2)

# Video capture
cap = cv2.VideoCapture(0)
MAX_THRESH = 20
count = 0

while True:
    ret, frame = cap.read()
    if not ret:
        break
    h, w, _ = frame.shape
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = face_mesh.process(frame_rgb)

    if results.multi_face_landmarks:
        for face_landmarks in results.multi_face_landmarks:
            landmarks = face_landmarks.landmark
            
            left_eye_ratio = get_blinking_ratio(LEFT_EYE, landmarks, w, h)
            right_eye_ratio = get_blinking_ratio(RIGHT_EYE, landmarks, w, h)
            blinking_ratio = (left_eye_ratio + right_eye_ratio) / 2

            if blinking_ratio > 5.0:
                cv2.putText(frame, "Blinking", (30, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)
                count += 1
                if count >= MAX_THRESH:
                    cv2.putText(frame, "Drowsiness Detected", (30, 450), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2)
            else:
                count = 0

    cv2.imshow("Blink & Drowsiness Detection", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
