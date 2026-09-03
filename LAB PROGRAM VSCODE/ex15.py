import cv2

# Read the image
img = cv2.imread("D:/Computer vision/sample images/images (4).jpg")

# Check whether the image is loaded
if img is None:
    print("Error: Image not found!")
else:
    # Apply Gaussian Blur
    blur = cv2.GaussianBlur(img, (7, 7), 0)

    # Display images
    cv2.imshow("Original Image", img)
    cv2.imshow("Blurred Image", blur)

    cv2.waitKey(0)
    cv2.destroyAllWindows()