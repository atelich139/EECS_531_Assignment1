import cv2 as cv
import numpy as np

# Reads the image into a variable
img = cv.imread('Exercise1_Image.jpg')


# Function to calculate the Gaussian transformation of a given point
def gaussian(x, y, sigma):
    g = np.multiply(np.divide(1, 2 * np.pi * np.power(sigma, 2)), np.exp(
        np.divide(-(np.power(x, 2) + np.power(y, 2)),
                  np.multiply(2, np.power(sigma, 2)))))
    return g


# Function to calculate the kernel matrix of an inputted size
# x: width, y: height
def kernel(x1, y1, sigma):
    w, h = x1, y1 - 1
    w2 = w / 2
    h2 = h / 2
    matrix = []
    for y in range(int(h2), int(-h2 - 1), -1):
        matrix.append([gaussian(x, y, sigma) for x in range(int(w2), int(-w2 - 1), -1)])
    return np.array(matrix)


# Function to convolude kernel matrix and image pixel matrix
def convolution(kernelMatrix, image):
    (imageHeight, imageWidth) = image.shape[:2]
    (kernelHeight, kernelWidth) = kernelMatrix.shape[:2]

    # Generates a padding based on kernel matrix width minus 1 and divided by 2
    padding = int(np.divide(kernelWidth - 1, 2))

    # Makes a border around the image with the size of the padding
    image = cv.copyMakeBorder(image, padding, padding, padding, padding,
                              cv.BORDER_REPLICATE)
    imageArray = np.array(image)

    # Convolution of the kernel matrix and the image pixel matrix
    for i in np.arange(padding, imageHeight + padding):
        for j in np.arange(padding, imageWidth + padding):
            patch = image[i - padding:i + padding + 1, j - padding:j + padding + 1]

            convolve = (patch * kernelMatrix).sum()

            imageArray[i - padding, j - padding] = convolve

    return imageArray


imageBlurred = convolution(kernel(3, 3, 0.84089642), img)

cv.imshow('image', imageBlurred)
cv.imwrite('Exercise1_OutputImage.png', imageBlurred)
cv.waitKey(0)
