import cv2

# Read the image
img = cv2.imread(r"D:\Computer vision\sample images\images (1).jpg")

# Check if the image is loaded
if img is None:
    print("Error: Image not found!")
else:
    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Detect edges using Canny
    edges = cv2.Canny(gray, 100, 200)

    # Display images
    cv2.imshow("Original Image", img)
    cv2.imshow("Canny Edge Detection", edges)

    # Wait until a key is pressed
    cv2.waitKey(0)
    cv2.destroyAllWindows()