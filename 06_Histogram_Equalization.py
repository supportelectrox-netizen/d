from PIL import Image
import matplotlib.pyplot as plt

image_path = "PNG/Task_06_Histogram_Equalization.png"
image = Image.open(image_path).convert("L")

width, height = image.size
pixels = image.load()

histogram = [0] * 256

for y in range(height):
    for x in range(width):
        intensity = pixels[x, y]
        histogram[intensity] += 1

cdf = [0] * 256
cdf[0] = histogram[0]

for i in range(1, 256):
    cdf[i] = cdf[i - 1] + histogram[i]

cdf_min = 0

for value in cdf:
    if value > 0:
        cdf_min = value
        break

total_pixels = width * height
denominator = total_pixels - cdf_min

mapping = [0] * 256

if denominator == 0:
    for i in range(256):
        mapping[i] = i
else:
    for i in range(256):
        new_intensity = (
            (cdf[i] - cdf_min) / denominator
        ) * 255

        new_intensity = max(0, min(255, new_intensity))

        mapping[i] = int(new_intensity + 0.5)

equalized_image = Image.new("L", (width, height))
equalized_pixels = equalized_image.load()

for y in range(height):
    for x in range(width):
        old_intensity = pixels[x, y]
        new_intensity = mapping[old_intensity]

        equalized_pixels[x, y] = new_intensity

equalized_histogram = [0] * 256

for y in range(height):
    for x in range(width):
        intensity = equalized_pixels[x, y]
        equalized_histogram[intensity] += 1

equalized_image.save("Output/histogram_equalized.png")

plt.figure(figsize=(12, 8))

plt.subplot(2, 2, 1)
plt.imshow(image, cmap="gray", vmin=0, vmax=255)
plt.title("Original Grayscale Image")
plt.axis("off")

plt.subplot(2, 2, 2)
plt.plot(range(256), histogram)
plt.title("Original Histogram")
plt.xlabel("Pixel Intensity")
plt.ylabel("Frequency")
plt.xlim(0, 255)

plt.subplot(2, 2, 3)
plt.imshow(equalized_image, cmap="gray", vmin=0, vmax=255)
plt.title("Histogram Equalized Image")
plt.axis("off")

plt.subplot(2, 2, 4)
plt.plot(range(256), equalized_histogram)
plt.title("Equalized Histogram")
plt.xlabel("Pixel Intensity")
plt.ylabel("Frequency")
plt.xlim(0, 255)

plt.tight_layout()
plt.show()

print("Histogram equalization completed successfully.")
print("Saved image: histogram_equalized.png")