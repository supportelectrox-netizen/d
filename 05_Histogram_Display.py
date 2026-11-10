from PIL import Image
import matplotlib.pyplot as plt

image = Image.open("PNG/Task_05_Grayscale_Histogram.png").convert("L")
width, height = image.size
pixels = image.load()

histogram = [0] * 256

for y in range(height):
    for x in range(width):
        intensity = pixels[x, y]
        histogram[intensity] += 1

plt.figure(figsize= (10, 4))

plt.subplot(1, 2, 1)
plt.imshow(image, cmap="gray", vmin=0, vmax=255)
plt.title("Grayscale Image")
plt.axis("off")

plt.subplot(1, 2, 2)
plt.bar(range(256), histogram, width=1.0)
plt.title("Grayscale Histogram")
plt.xlabel("Pixel Intensity")
plt.ylabel("Number of Pixels")
plt.xlim(0, 255)

plt.tight_layout()
plt.show()