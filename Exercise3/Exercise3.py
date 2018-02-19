import cv2 as cv
import numpy as np

image = cv.imread('Exercise3_Image.jpg')
imageGrey = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
imageGrey = np.float32(imageGrey)

dst = cv.cornerHarris(imageGrey, 2, 3, 0.04)
dst = cv.dilate(dst, None)

image[dst > 0.08 * dst.max()] = [0, 0, 255]

cv.imshow('dst', imageGrey)
cv.waitKey(0)

