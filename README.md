# 🎛️ Hand Gesture Volume Controller

A real-time Computer Vision project that allows users to control the Windows system volume using hand gestures. The application uses a webcam to track the distance between the thumb and index finger and adjusts the system volume accordingly.

## 🚀 Features

* Real-time hand detection and tracking
* Gesture-based volume control
* Live webcam feed with visual hand landmarks
* Dynamic volume percentage display
* Windows system volume integration
* Fast and lightweight implementation

## 🛠️ Technologies Used

* Python
* OpenCV
* MediaPipe
* NumPy
* Pycaw

## 📌 How It Works

1. The webcam captures live video frames.
2. MediaPipe detects and tracks hand landmarks.
3. The thumb tip (Landmark 4) and index finger tip (Landmark 8) are identified.
4. The Euclidean distance between these landmarks is calculated.
5. NumPy's interpolation function maps the distance range to a volume range.
6. Pycaw communicates with the Windows Audio API to adjust the system volume in real time.

## 📷 Project Workflow

Hand Detection → Landmark Tracking → Distance Calculation → Volume Mapping → Windows Volume Control

## ⚙️ Installation

### Clone the Repository

```bash
git clone https://github.com/BalrajSahu/Hand-Gesture-Volume-Controller.git
cd Hand-Gesture-Volume-Controller
```

### Install Dependencies

```bash
pip install opencv-python mediapipe numpy pycaw comtypes
```

### Run the Project

```bash
python cor.py
```

## 🎯 Usage

* Bring your thumb and index finger close together to decrease volume.
* Move your thumb and index finger apart to increase volume.
* Watch the volume percentage update in real time on the screen.

## 🧠 Concepts Learned

* Computer Vision
* Hand Tracking
* MediaPipe Landmarks
* OpenCV Image Processing
* Euclidean Distance Calculation
* Interpolation using NumPy
* Windows Audio Control with Pycaw

## 📈 Future Improvements

* Volume Bar UI
* FPS Counter
* Gesture Smoothing
* Mute Gesture
* Multi-Hand Support
* Custom Gesture Controls

## 👨‍💻 Author

**Balraj Sahu**

Aspiring AI Engineer | Python Developer | Computer Vision Enthusiast

---

⭐ If you found this project useful, consider giving it a star!
