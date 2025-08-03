Here’s a professional and complete `README.md` for your **Blink and Drowsiness Detection using MediaPipe** project:

---

# 👁️ Blink and Drowsiness Detection using MediaPipe & OpenCV

This real-time computer vision project uses **MediaPipe Face Mesh** and **OpenCV** to detect blinks and prolonged eye closure — a common sign of **drowsiness**. It calculates the **eye aspect ratio (EAR)** using facial landmarks to monitor blinking and trigger alerts if the eyes remain closed for too long.

---

## 📹 Features

* Detects **eye blinks** using facial landmarks.
* Monitors blink duration and frequency.
* Triggers **drowsiness alert** if eyes remain closed for extended frames.
* Runs in real-time on webcam feed using OpenCV.

---

## 🧰 Requirements

Install the necessary Python libraries:

```bash
pip install opencv-python mediapipe numpy
```

---

## 🧠 How It Works

1. **MediaPipe Face Mesh** tracks 468 facial landmarks.
2. Selects 6 landmarks per eye to compute the eye aspect ratio.
3. Calculates horizontal and vertical eye distances.
4. If vertical distance becomes too small compared to horizontal → **blink** detected.
5. If this blink lasts over a threshold (e.g., 20 consecutive frames) → **Drowsiness alert** is triggered.

---

## 🧾 Eye Landmarks Used

* **Left Eye**: `[362, 385, 387, 263, 373, 380]`
* **Right Eye**: `[33, 160, 158, 133, 153, 144]`

These landmark indices are from MediaPipe's 468-point face mesh model.

---

## 🎯 Detection Logic

* Calculates:

  ```python
  blinking_ratio = horizontal_length / vertical_length
  ```
* Threshold:

  * If `blinking_ratio > 5.0` → Eye is likely **closed**
  * If closed for `MAX_THRESH` (20) frames → **Drowsiness Detected**

---

## 📂 Project Structure

```
📁 your_project_folder/
├── 📄 drowsiness_detection.py  # Main script
└── 📁 requirements.txt         # Optional: for dependencies
```

---

## 📷 Sample Output

When running:

* "Blinking" text appears when a blink is detected.
* "Drowsiness Detected" shows in red when eyes are closed too long.

| 🟢 Blink Detected            | 🔴 Drowsiness Alert            |
| ---------------------------- | ------------------------------ |
| ![Blink](./sample_blink.jpg) | ![Drowsy](./sample_drowsy.jpg) |

> *(Replace the images above with your actual captured frames)*

---

## ▶️ How to Run

```bash
python drowsiness_detection.py
```

* Press **`q`** to quit the live feed.

---

## 🛠️ Customization

* Adjust sensitivity:

  ```python
  MAX_THRESH = 20        # How many frames to wait before alert
  blinking_ratio > 5.0   # Blink threshold
  ```
* For multi-face support, increase `max_num_faces`.

---

## 📝 License

This project is open-source and available under the MIT License.

---

## 🙌 Acknowledgements

* [MediaPipe](https://github.com/google/mediapipe)
* [OpenCV](https://opencv.org/)
* Eye landmark detection inspired by facial aspect ratio (EAR) concepts in drowsiness research.

---

Let me know if you'd like a version with webcam snapshot saving, email alerts, or integrated sound warnings.
