import numpy as np

# Setting up the Gaussian transformation function
x = 0  # Set to the x coordinate of the pixel
y = 0  # Set to the y coordinate of the pixel
sigma = 0.84089642  # Standard deviation of Gaussian distribution
gaussian = (1 / 2 * np.pi * sigma ^ 2) * np.e ^ (-(((x ^ 2) + (y ^ 2)) / (2 * sigma ^ 2)))

# TODO algorithm for calculating Gaussian transformation for each element in pixel matrix

# Defines the 5x5 kernel matrix
w1, h1 = 5, 5
kernelMatrix = []
for y in range(h1):
    kernelMatrix.append([0 for x in range(w1)])

# Defines the 5x5 pixel matrix
w2, h2 = 5, 5
pixelMatrix = []
for y in range(h2):
    pixelMatrix.append([0 for x in range(w2)])

# TODO set up logic for inputting an image
# TODO outer for loop to iterate through image pixels

# Variable for result of convolution for each pixel and kernel
accumulator = 0

# Double for-loop to handle convolution with pixel matrices from image
for j in range(w1):
    for i in range(h1):
        product = kernelMatrix[j][i] * pixelMatrix[j][i]
        accumulator = accumulator + product

# Once done with convolution for each pixel set output image pixel equal to accumulator

