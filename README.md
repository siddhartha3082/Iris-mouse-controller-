# Iris Mouse Controller

This project allows you to control the mouse cursor using eye movement. 
It uses Mediapipe FaceMesh for landmark detection and OpenCV for processing, 
while PyAutoGUI is used to move the cursor and handle clicks.

## Features
- Real-time eye tracking
- Cursor movement mapped to eye direction
- Blink-based clicking
- Smooth movement filtering
- Works offline

## Installation
Install required packages:
```
pip install -r requirements.txt
```

## Usage
Run the script:
```
python iris_mouse_controller.py
```

Controls:
- Move your eyes to move the cursor
- Blink to click
- Press Q to exit

## Requirements
```
opencv-python
mediapipe
pyautogui
```

## Author
Siddhartha Reddy  
GitHub: https://github.com/siddhartha3082
