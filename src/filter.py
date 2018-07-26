import cv2
import numpy as np

def grayscale(img):
    return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

def canny(img, low_threshold, high_threshold):
    return cv2.Canny(img, low_threshold, high_threshold)

def gaussian_blur(img, kernel_size):
    return cv2.GaussianBlur(img, (kernel_size, kernel_size), 0)

img = cv2.imread("test_files/test01.jpg")

img1 = grayscale(img)
cv2.imshow("01", img1)
cv2.waitKey()

img2 = canny(img1, 200, 255)
cv2.imshow("02", img2)
cv2.waitKey()

img3 = gaussian_blur(img2, 3)
cv2.imshow("03", img3)

cv2.waitKey()
cv2.destroyAllWindows()
