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

# TODO algorithm for calculating Gaussian for each element in pixel matrix
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
