import cv2

# Read the image
img = cv2.imread (r"D:\Computer vision\sample images\images (1).jpg")

# Check whether the image is loaded
if img is None:
    print("Error: Image not found!")
else:
    # Apply Gaussian Blur
    blur = cv2.GaussianBlur(img, (7, 7), 0)

    # Display original image
    cv2.imshow("Original Image", img)

    # Display blurred image
    cv2.imshow("Blurred Image", blur)

    # Wait for a key press
    cv2.waitKey(0)

    # Close all windows
    cv2.destroyAllWindows()