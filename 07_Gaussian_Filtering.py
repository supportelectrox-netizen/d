from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import math

image = Image.open("PNG/Task_07_Gaussian_Filtering.png").convert("RGB")
image_array = np.array(image, dtype=np.float64)

height, width, channels = image_array.shape

kernel_size = 5
sigma = 1.0

radius = kernel_size // 2

kernel = np.zeros((kernel_size, kernel_size), dtype=np.float64)

for i in range(kernel_size):
    for j in range(kernel_size):

        x = j - radius
        y = i - radius

        value = (1 / (2 * math.pi * sigma ** 2)) * math.exp(
            -(x ** 2 + y ** 2) / (2 * sigma ** 2)
        )

        kernel[i, j] = value

kernel_sum = np.sum(kernel)
kernel = kernel / kernel_sum

print("Gaussian Kernel:")
print(np.round(kernel, 4))

filtered_image = np.zeros(
    (height, width, channels),
    dtype=np.uint8
)

for y in range(height):
    for x in range(width):

        for c in range(channels):

            pixel_sum = 0.0

            for ky in range(kernel_size):
                for kx in range(kernel_size):
                    input_y = y + ky - radius
                    input_x = x + kx - radius
                    if input_y < 0:
                        input_y = 0
                    elif input_y >= height:
                        input_y = height - 1

                    if input_x < 0:
                        input_x = 0
                    elif input_x >= width:
                        input_x = width - 1
                    pixel_value = image_array[input_y, input_x, c]
                    kernel_value = kernel[ky, kx]

                    pixel_sum += pixel_value * kernel_value
            pixel_sum = max(0, min(255, pixel_sum))

            filtered_image[y, x, c] = int(round(pixel_sum))

output_image = Image.fromarray(filtered_image)
output_image.save("gaussian_filtered.png")

plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.imshow(image_array.astype(np.uint8))
plt.title("Original Image")
plt.axis("off")

plt.subplot(1, 2, 2)
plt.imshow(filtered_image)
plt.title("Gaussian Filtered Image")
plt.axis("off")

plt.tight_layout()
plt.show()

print("Gaussian filtering completed successfully.")
print("Output saved as gaussian_filtered.png")