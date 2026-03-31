##  Description

This project uses hand‑gesture detection to control the Chrome Dino game through the webcam. The system tracks the hand in real time and measures the distance between the thumb and index finger. When the fingers come close together, the script sends a **Space** key input, which makes the dinosaur jump.

***

##  Features

*   Real‑time hand tracking 
*   Pinch‑gesture detection using finger distance 📏
*   Sends **Space** input to control the Dino game 🎮
*   Works with any standard webcam 🖥️
*   Lightweight and easy to run ⚡

***

##  Tech Used

*   Python
*   OpenCV
*   CVZone
*   Mediapipe
*   PyAutoGUI

***

##  How It Works

*   Captures video from the webcam
*   Detects and tracks hand landmark points
*   Checks the distance between the thumb and index finger
*   When the distance is small enough, it triggers a **Space** key press
*   Allows you to play the Chrome Dino game using hand gestures instead of the keyboard

***
