import cv2
import random
import time
from cvzone.HandTrackingModule import HandDetector

# Webcam setup
cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)

# Hand detector setup
detector = HandDetector(maxHands=1, detectionCon=0.8)

# Game settings
circle_radius = 40
circle_x = random.randint(100, 1180)
circle_y = random.randint(100, 620)

score = 0
game_time = 30
start_time = time.time()

while True:
    success, img = cap.read()

    if not success:
        print("Failed to access webcam")
        break

    # Flip image for mirror effect
    img = cv2.flip(img, 1)

    # Calculate remaining time
    elapsed_time = time.time() - start_time
    remaining_time = int(game_time - elapsed_time)

    # Detect hands
    hands, img = detector.findHands(img, flipType=False)

    if remaining_time > 0:
        # Draw circle
        cv2.circle(img, (circle_x, circle_y), circle_radius, (0, 255, 0), cv2.FILLED)

        if hands:
            hand = hands[0]
            lmList = hand["lmList"]

            # Index finger tip landmark is number 8
            index_finger = lmList[8]
            finger_x, finger_y = index_finger[0], index_finger[1]

            # Draw small circle on index finger
            cv2.circle(img, (finger_x, finger_y), 10, (255, 0, 255), cv2.FILLED)

            # Measure distance between index finger and circle center
            distance, info, img = detector.findDistance(
                (finger_x, finger_y),
                (circle_x, circle_y),
                img
            )

            # Check if finger catches the circle
            if distance <= circle_radius:
                score += 1

                # Move circle to a new random position
                circle_x = random.randint(100, 1180)
                circle_y = random.randint(100, 620)

        # Display score and timer
        cv2.putText(img, f"Score: {score}", (50, 80),
                    cv2.FONT_HERSHEY_SIMPLEX, 1.5, (255, 0, 0), 3)

        cv2.putText(img, f"Time: {remaining_time}", (1000, 80),
                    cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 0, 255), 3)

    else:
        # Game over screen
        cv2.putText(img, "GAME OVER", (420, 300),
                    cv2.FONT_HERSHEY_SIMPLEX, 2.5, (0, 0, 255), 5)

        cv2.putText(img, f"Final Score: {score}", (430, 400),
                    cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 0, 0), 4)

        cv2.putText(img, "Press Q to Exit", (450, 500),
                    cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 0, 0), 3)

    # Show the game window
    cv2.imshow("Catch the Circle Game", img)

    # Exit when pressing q
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
