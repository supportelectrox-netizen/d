import numpy as np
import matplotlib.pyplot as plt

image = plt.imread("PNG/Task_11_Salt_Pepper_Noise_Restoration.png")

if image.ndim == 3:
    image = (0.299 * image[:, :, 0] +
             0.587 * image[:, :, 1] +
             0.114 * image[:, :, 2])
if image.max() <= 1:
    image = image * 255

image = image.astype(np.uint8)

def add_salt_pepper_noise(image, noise_ratio=0.05):
    noisy_image = image.copy()
    total_pixels = image.size
    num_noise = int(total_pixels * noise_ratio)

    random_positions = np.random.randint(
        0, total_pixels, num_noise
    )

    half = num_noise // 2
    flat_image = noisy_image.flatten()
    flat_image[random_positions[:half]] = 255
    flat_image[random_positions[half:]] = 0
    noisy_image = flat_image.reshape(image.shape)
    return noisy_image

def median_filter(image, kernel_size=3):
    height, width = image.shape
    padding = kernel_size // 2
    padded_image = np.pad(
        image,
        padding,
        mode='edge'
    )

    filtered_image = np.zeros_like(image)

    for i in range(height):
        for j in range(width):
            window = padded_image[
                i:i + kernel_size,
                j:j + kernel_size
            ]

            values = sorted(window.flatten())
            median_value = values[len(values) // 2]
            filtered_image[i, j] = median_value

    return filtered_image

noisy_image = add_salt_pepper_noise(
    image,
    noise_ratio=0.05
)
restored_image = median_filter(
    noisy_image,
    kernel_size=3
)
plt.figure(figsize=(15, 5))

plt.subplot(1, 3, 1)
plt.imshow(image, cmap='gray')
plt.title("Original Image")
plt.axis("off")

plt.subplot(1, 3, 2)
plt.imshow(noisy_image, cmap='gray')
plt.title("Salt-and-Pepper Noisy Image")
plt.axis("off")

plt.subplot(1, 3, 3)
plt.imshow(restored_image, cmap='gray')
plt.title("Restored Image (Median Filter)")
plt.axis("off")

plt.tight_layout()
plt.show()
