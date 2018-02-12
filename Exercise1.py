# Defines the 5x5 kernel matrix
w, h = 5, 5
kernelMatrix = []
for y in range(h):
    kernelMatrix.append([0 for x in range(w)])

# Double for-loop to handle convolution with pixel matrices from image
for j in range(w):
    for i in range(h):
        print(kernelMatrix[j][i]);