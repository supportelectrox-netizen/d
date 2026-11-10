import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

image_path = "PNG/Task_09_Ideal_Low_Pass_Filter.png"

image = Image.open(image_path).convert("L")
img = np.array(image, dtype=np.float64)

rows, cols = img.shape
fourier = np.fft.fft2(img)

fourier_shifted = np.fft.fftshift(fourier)
spectrum = 20 * np.log(1 + np.abs(fourier_shifted))

D0 = 30
crow = rows // 2
ccol = cols // 2

mask = np.zeros((rows, cols), dtype=np.float64)

for u in range(rows):
    for v in range(cols):

        distance = np.sqrt((u - crow) ** 2 + (v - ccol) ** 2)
        if distance <= D0:
            mask[u, v] = 1
        else:
            mask[u, v] = 0

filtered_fourier = fourier_shifted * mask
filtered_spectrum = 20 * np.log(1 + np.abs(filtered_fourier))

inverse_shifted = np.fft.ifftshift(filtered_fourier)
filtered_image = np.fft.ifft2(inverse_shifted)
filtered_image = np.real(filtered_image)
filtered_image = np.clip(filtered_image, 0, 255)
filtered_image = filtered_image.astype(np.uint8)

result = Image.fromarray(filtered_image)
result.save("Output/ideal_low_pass_filtered.png")

plt.figure(figsize=(15, 9))

plt.subplot(2, 3, 1)
plt.imshow(img, cmap="gray")
plt.title("Original Grayscale Image")
plt.axis("off")

plt.subplot(2, 3, 2)
plt.imshow(spectrum, cmap="gray")
plt.title("Fourier Transform Spectrum")
plt.axis("off")

plt.subplot(2, 3, 3)
plt.imshow(mask, cmap="gray")
plt.title("Ideal Low-Pass Filter Mask")
plt.axis("off")

plt.subplot(2, 3, 4)
plt.imshow(filtered_spectrum, cmap="gray")
plt.title("Filtered Frequency Spectrum")
plt.axis("off")

plt.subplot(2, 3, 5)
plt.imshow(filtered_image, cmap="gray")
plt.title("ILPF Output Image")
plt.axis("off")

plt.tight_layout()
plt.show()

print("Ideal Low-Pass Filtering completed successfully!")
print("Filtered image saved as ideal_low_pass_filtered.png")
