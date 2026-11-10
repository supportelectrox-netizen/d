import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

image = Image.open("PNG/Task_13_Morphological_Dilation.png").convert("L")
gray_image = np.array(image)

threshold = 128
height, width = gray_image.shape

binary_image = np.zeros((height, width), dtype=np.uint8)

for i in range(height):
    for j in range(width):
        if gray_image[i, j] >= threshold:
            binary_image[i, j] = 255
        else:
            binary_image[i, j] = 0

kernel = np.array([
    [1, 1, 1],
    [1, 1, 1],
    [1, 1, 1]
])

kernel_height, kernel_width = kernel.shape
pad_height = kernel_height // 2
pad_width = kernel_width // 2
padded_image = np.zeros(
    (height + 2 * pad_height, width + 2 * pad_width),
    dtype=np.uint8
)

padded_image[
    pad_height:pad_height + height,
    pad_width:pad_width + width
] = binary_image

dilated_image = np.zeros((height, width), dtype=np.uint8)

for i in range(height):
    for j in range(width):
        for ki in range(kernel_height):
            for kj in range(kernel_width):

                if kernel[ki, kj] == 1:

                    if padded_image[i + ki, j + kj] == 255:
                        dilated_image[i, j] = 255

plt.figure(figsize=(12, 5))

plt.subplot(1, 3, 1)
plt.imshow(gray_image, cmap='gray')
plt.title("Original Grayscale Image")
plt.axis("off")

plt.subplot(1, 3, 2)
plt.imshow(binary_image, cmap='gray')
plt.title("Binary Image")
plt.axis("off")

plt.subplot(1, 3, 3)
plt.imshow(dilated_image, cmap='gray')
plt.title("Dilated Image")
plt.axis("off")

plt.tight_layout()
plt.show()

Image.fromarray(dilated_image).save("Output/dilated_output.png")

print("Morphological Dilation Completed Successfully!")