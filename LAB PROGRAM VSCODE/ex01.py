import cv2

path = r"D:\Computer vision\sample images\images (4).jpg"

img = cv2.imread(path)

if img is None:
    print("Image not found!")
    print(path)
else:
    print("Image loaded successfully.")

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    cv2.imshow("Original", img)
    cv2.imshow("Gray", gray)

    cv2.waitKey(0)
    cv2.destroyAllWindows()