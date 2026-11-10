import numpy as np
import matplotlib.pyplot as plt

image = np.array([
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 1, 1, 1, 0, 0],
    [0, 1, 1, 1, 1, 1, 1, 0, 0],
    [0, 1, 1, 1, 1, 1, 1, 0, 0],
    [0, 1, 1, 1, 1, 1, 1, 0, 0],
    [0, 1, 1, 1, 1, 1, 1, 0, 0],
    [0, 1, 1, 1, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]
], dtype=np.uint8)

kernel = np.ones((3, 3), dtype=np.uint8)
rows, cols = image.shape
k_rows, k_cols = kernel.shape
pad_y = k_rows // 2
pad_x = k_cols // 2

padded_image = np.zeros(
    (rows + 2 * pad_y, cols + 2 * pad_x),
    dtype=np.uint8
)

padded_image[
    pad_y:pad_y + rows,
    pad_x:pad_x + cols
] = image

eroded_image = np.zeros_like(image)

for i in range(rows):
    for j in range(cols):
        neighborhood = padded_image[
            i:i + k_rows,
            j:j + k_cols
        ]
        if np.all(neighborhood[kernel == 1] == 1):
            eroded_image[i, j] = 1
        else:
            eroded_image[i, j] = 0
            
plt.figure(figsize=(10, 4))

plt.subplot(1, 2, 1)
plt.imshow(image, cmap='gray', vmin=0, vmax=1)
plt.title("Original Binary Image")
plt.axis("off")

plt.subplot(1, 2, 2)
plt.imshow(eroded_image, cmap='gray', vmin=0, vmax=1)
plt.title("Eroded Image")
plt.axis("off")

plt.tight_layout()
plt.show()
