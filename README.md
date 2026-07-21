# Catch the Circle - Computer Vision Game

## Introduction

Catch the Circle is an interactive computer vision game built using Python. The game uses the webcam to track the player’s hand in real time. The player uses the index finger to catch a randomly appearing circle on the screen before the timer ends.

## Project Idea

A circle appears at a random position on the screen. The webcam tracks the user’s hand and detects the position of the index finger. When the index finger touches the circle, the score increases and the circle moves to a new random location.

The goal of the project is to practice basic computer vision concepts in a fun and interactive way.

## Technologies Used

- Python
- OpenCV
- cvzone
- MediaPipe
- random
- time

## Features

- Real-time webcam video capture
- Hand tracking using computer vision
- Index finger tracking using hand landmarks
- Random circle generation
- Distance-based collision detection
- Score counter
- Countdown timer
- Game Over screen
- Exit using the `q` key

## How the Game Works

1. The webcam is initialized using OpenCV.
2. The hand is detected using `cvzone.HandTrackingModule`.
3. The index finger tip is tracked using landmark number 8.
4. A filled circle is drawn at a random position on the screen.
5. The distance between the index finger and the circle center is calculated.
6. If the distance is less than or equal to the circle radius, the circle is caught.
7. The score increases by one.
8. The circle moves to a new random position.
9. The timer continues counting down until the game ends.


