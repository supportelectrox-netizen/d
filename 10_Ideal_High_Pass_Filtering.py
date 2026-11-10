import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

image_path = "PNG/Task_10_Ideal_High_Pass_Filter.png"

img = Image.open(image_path).convert("RGB")
img_array = np.asarray(img, dtype=np.float32)

gray = (
    0.299 * img_array[:, :, 0] +
    0.587 * img_array[:, :, 1] +
    0.114 * img_array[:, :, 2]
)

F = np.fft.fft2(gray)
F_shifted = np.fft.fftshift(F)

rows, cols = gray.shape
center_row = rows // 2
center_col = cols // 2
D0 = 30
mask = np.zeros((rows, cols), dtype=np.float32)

for i in range(rows):
    for j in range(cols):
        distance = np.sqrt((i - center_row) ** 2 +(j - center_col) ** 2)
        if distance > D0:
            mask[i, j] = 1

G = F_shifted * mask
G_ishift = np.fft.ifftshift(G)
filtered_image = np.fft.ifft2(G_ishift)
filtered_image = np.real(filtered_image)
min_val = np.min(filtered_image)
max_val = np.max(filtered_image)

if max_val > min_val:
    output = (filtered_image - min_val) / (max_val - min_val)
    output = output * 255
else:
    output = np.zeros_like(filtered_image)

plt.figure(figsize=(15, 5))

plt.subplot(1, 4, 1)
plt.imshow(gray, cmap="gray")
plt.title("Original Grayscale Image")
plt.axis("off")

plt.subplot(1, 4, 2)
plt.imshow(np.log(1 + np.abs(F_shifted)), cmap="gray")
plt.title("Frequency Spectrum")
plt.axis("off")

plt.subplot(1, 4, 3)
plt.imshow(mask, cmap="gray")
plt.title("Ideal High-Pass Filter Mask")
plt.axis("off")

plt.subplot(1, 4, 4)
plt.imshow(output, cmap="gray")
plt.title("Ideal High-Pass Filtered Image")
plt.axis("off")

plt.tight_layout()
plt.show()