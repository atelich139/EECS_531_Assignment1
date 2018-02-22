import cv2 as cv
import numpy as np

# Reads the image into a variable
img = cv.imread('dynboard.png', 0)


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
def findCorners(kernelMatrix, image, k, threshold):
    (imageHeight, imageWidth) = np.gradient(image)
    (kernelHeight, kernelWidth) = kernelMatrix.shape[:2]
    height = image.shape[0]
    width = image.shape[1]

    Ixx = imageWidth ** 2
    Ixy = imageHeight * imageWidth
    Iyy = imageHeight ** 2

    # Generates a padding based on kernel matrix width divided by 2
    padding = int(kernelWidth / 2)

    # Makes a border around the image with the size of the padding
    image = cv.copyMakeBorder(image, padding, padding, padding, padding,
                              cv.BORDER_REPLICATE)
    imageArray = image
    coloredImage = cv.cvtColor(imageArray, cv.COLOR_GRAY2RGB)

    corners = []

    # Sum of squares
    for i in range(padding, height - padding):
        for j in range(padding, width - padding):
            patchIxx = Ixx[i - padding:i + padding + 1, j - padding:j + padding + 1]
            patchIxy = Ixy[i - padding:i + padding + 1, j - padding:j + padding + 1]
            patchIyy = Iyy[i - padding:i + padding + 1, j - padding:j + padding + 1]

            Sxx = patchIxx.sum()
            Sxy = patchIxy.sum()
            Syy = patchIyy.sum()

            # Use the Gaussian kernel I made from Exercise 1
            a = (Sxx * kernelMatrix).sum()
            b = (Sxy * kernelMatrix).sum()
            c = (Syy * kernelMatrix).sum()

            # Find det and trace
            det = (a * c) - (b ** 2)
            trace = a + c

            # Find the limit for a corner
            r = det - k * (trace ** 2)

            if r > threshold:
                corners.append([j, i, r])
                coloredImage.itemset((i, j, 0), 83)
                coloredImage.itemset((i, j, 1), 255)
                coloredImage.itemset((i, j, 2), 62)

    print(corners)
    return coloredImage


imageMarked = findCorners(kernel(3, 3, 0.84089642), img, 0.2, 1)

cv.imshow('imageMarked', imageMarked)
cv.imwrite('Exercise3_OutputImage.png', imageMarked)
cv.waitKey(0)
