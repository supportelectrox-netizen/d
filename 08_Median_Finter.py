from PIL import Image
import matplotlib.pyplot as plt

input_path = "PNG/Task_08_Median_Filtering.png"
output_path = "Output/median_filtered.png"

image = Image.open(input_path)

if image.mode == "L":
    image = image.convert("L")
else:
    image = image.convert("RGB")

width, height = image.size
pixels = image.load()

kernel_size = 3
radius = kernel_size // 2

if kernel_size < 1 or kernel_size % 2 == 0:
    raise ValueError("Kernel size must be a positive odd number.")

filtered_image = Image.new(image.mode, (width, height))
output_pixels = filtered_image.load()

channel_count = 1 if image.mode == "L" else 3

for y in range(height):
    for x in range(width):

        neighborhoods = [[] for _ in range(channel_count)]
        for dy in range(-radius, radius + 1):
            for dx in range(-radius, radius + 1):
                nx = min(max(x + dx, 0), width - 1)
                ny = min(max(y + dy, 0), height - 1)

                pixel = pixels[nx, ny]

                if channel_count == 1:
                    neighborhoods[0].append(pixel)
                else:
                    for c in range(channel_count):
                        neighborhoods[c].append(pixel[c])

        median_values = []

        for values in neighborhoods:
            values.sort()
            middle = len(values) // 2
            median_values.append(values[middle])

        if channel_count == 1:
            output_pixels[x, y] = median_values[0]
        else:
            output_pixels[x, y] = tuple(median_values)

filtered_image.save(output_path)

print("Median Filtering Completed!")
print("Output saved as:", output_path)

plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
if image.mode == "L":
    plt.imshow(image, cmap="gray", vmin=0, vmax=255)
else:
    plt.imshow(image)
plt.title("Original Image")
plt.axis("off")

plt.subplot(1, 2, 2)
if filtered_image.mode == "L":
    plt.imshow(filtered_image, cmap="gray", vmin=0, vmax=255)
else:
    plt.imshow(filtered_image)
plt.title("Median Filtered Image")
plt.axis("off")

plt.tight_layout()
plt.show()
