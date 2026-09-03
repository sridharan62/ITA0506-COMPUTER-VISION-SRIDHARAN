import cv2

# Read the video
cap = cv2.VideoCapture(r"C:\Users\mothi\Documents\22.mp4")

# Check if video is opened
if not cap.isOpened():
    print("Error: Unable to open video.")
else:
    while True:
        ret, frame = cap.read()

        if not ret:
            break

        cv2.imshow("Slow Motion Video", frame)

        # Slow motion (100 ms delay)
        if cv2.waitKey(100) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()