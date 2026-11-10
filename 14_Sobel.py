
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

image = Image.open("PNG/Task_14_Sobel_Edge_Detection.png").convert("L")
img = np.array(image, dtype=np.float64)

rows, cols = img.shape

Gx = np.array([
    [-1, 0, 1],
    [-2, 0, 2],
    [-1, 0, 1]
])

Gy = np.array([
    [-1, -2, -1],
    [ 0,  0,  0],
    [ 1,  2,  1]
])

gradient_x = np.zeros((rows, cols))
gradient_y = np.zeros((rows, cols))
edge_image = np.zeros((rows, cols))

for i in range(1, rows - 1):
    for j in range(1, cols - 1):

        sum_x = 0
        sum_y = 0

        for m in range(-1, 2):
            for n in range(-1, 2):

                pixel = img[i + m, j + n]

                sum_x += pixel * Gx[m + 1, n + 1]
                sum_y += pixel * Gy[m + 1, n + 1]

        gradient_x[i, j] = sum_x
        gradient_y[i, j] = sum_y
for i in range(rows):
    for j in range(cols):

        edge_image[i, j] = np.sqrt(
            gradient_x[i, j] ** 2 +
            gradient_y[i, j] ** 2
        )
max_value = np.max(edge_image)

if max_value > 0:
    edge_image = (edge_image / max_value) * 255

edge_image = edge_image.astype(np.uint8)

plt.figure(figsize=(12, 5))

plt.subplot(1, 3, 1)
plt.imshow(img, cmap="gray")
plt.title("Original Image")
plt.axis("off")

plt.subplot(1, 3, 2)
plt.imshow(gradient_x, cmap="gray")
plt.title("Horizontal Gradient (Gx)")
plt.axis("off")

plt.subplot(1, 3, 3)
plt.imshow(edge_image, cmap="gray")
plt.title("Sobel Edge Detection")
plt.axis("off")

plt.tight_layout()
plt.show()
