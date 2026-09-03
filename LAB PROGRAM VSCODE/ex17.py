import cv2

img = cv2.imread("D:/Computer vision/sample images/images (4).jpg")

if img is None:
    print("Error: Image not found!")
else:
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    sobelx = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)

    cv2.imshow("Original Image", img)
    cv2.imshow("Sobel X", sobelx)

    cv2.waitKey(0)
    cv2.destroyAllWindows()