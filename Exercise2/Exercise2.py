import cv2 as cv
from matplotlib import pyplot as plot


# Loads the image in greyscale
image = cv.imread('Exercise2_Image.jpg', 0)

# Uses Canny method to detect edges
#
# The 2nd and 3rd inputs to this method are the minVal and maxVal of the
# threshold, respectively.
#
# The 4th value is the size of the 'patch'
#
# The 5th value is whether or not to use the Canny Algorithm
edges = cv.Canny(image, 100, 400, apertureSize=5, L2gradient=True)

# Plots the image's detected edges
plot.subplot(), plot.imshow(edges, cmap='gray')
plot.show()
