# 🛻 Raspberry Pi Remote Car

This is a Raspberry Pi-based remote-controlled car, controllable through a web interface with live video streaming and keyboard input.

## 🚀 Features
- Live camera feed from PiCam
- Motor control via keyboard (Arrow keys)
- Flask web server
- GPIO control for motors
- Stream flipped/inverted video feed for proper orientation

## 📸 Demo
![Screenshot](/remoteCarCamera/IMG_0689.PNG)

## 🎥 Video Demo
[![Watch the video](https://drive.google.com/file/d/1s1xCsv4QrY7cBPhAIoiak7AM42_--g8b/view?usp=drive_link)]

## 🧰 Tech Stack
- Python + Flask
- OpenCV
- Picamera2
- HTML/JS frontend
- GPIO control

## 🔧 Wiring
| GPIO Pin | Function       |
|----------|----------------|
| 22       | Left Motor FWD |
| 27       | Left Motor REV |
| 23       | Right Motor FWD|
| 24       | Right Motor REV|

## 🛠 How to Run
```bash
python3 app.py
