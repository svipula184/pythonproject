import cv2
import numpy as np

# Open webcam
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Cannot open webcam")
    exit()

# Function to recognize color
def detect_color(h, s, v):

    if v < 50:
        return "Black"

    if s < 40:
        if v > 200:
            return "White"
        else:
            return "Gray"

    if 0 <= h <= 10 or 170 <= h <= 179:
        return "Red"

    elif 11 <= h <= 20:
        return "Orange"

    elif 21 <= h <= 35:
        return "Yellow"

    elif 36 <= h <= 85:
        return "Green"

    elif 86 <= h <= 125:
        return "Blue"

    elif 126 <= h <= 145:
        return "Purple"

    elif 146 <= h <= 169:
        return "Pink"

    return "Unknown"

while True:

    ret, frame = cap.read()

    if not ret:
        break

    frame = cv2.flip(frame, 1)

    height, width, _ = frame.shape

    cx = width // 2
    cy = height // 2

    # Draw center rectangle
    cv2.rectangle(frame,
                  (cx - 20, cy - 20),
                  (cx + 20, cy + 20),
                  (0, 255, 255),
                  2)

    # Read color from center
    bgr = frame[cy, cx]

    hsv = cv2.cvtColor(
        np.uint8([[bgr]]),
        cv2.COLOR_BGR2HSV
    )[0][0]

    H = int(hsv[0])
    S = int(hsv[1])
    V = int(hsv[2])

    color = detect_color(H, S, V)

    B = int(bgr[0])
    G = int(bgr[1])
    R = int(bgr[2])

    # Display information
    cv2.putText(frame,
                f"Detected Color : {color}",
                (20, 40),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.9,
                (0, 255, 0),
                2)

    #cv2.putText(frame,
            #  #  f"HSV : ({H}, {S}, {V})",
              #  (20, 80),
              #  cv2.FONT_HERSHEY_SIMPLEX,
              #  0.7,
              #  (255, 255, 255),
              #  2)

    #cv2.putText(frame,
              #  f"RGB : ({R}, {G}, {B})",
              #  (20, 120),
              #  cv2.FONT_HERSHEY_SIMPLEX,
              #  0.7,
              #  (255, 255, 255),
              #  2)

    cv2.imshow("Color Recognizer", frame)

    key = cv2.waitKey(1)

    if key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()