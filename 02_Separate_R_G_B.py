from PIL import Image
import matplotlib.pyplot as plt

image = Image.open("PNG/Task_02_Separate_RGB_Channels.png").convert("RGB")

width, height = image.size

red_image = Image.new("RGB", (width, height))
green_image = Image.new("RGB", (width, height))
blue_image = Image.new("RGB", (width, height))

red_pixels = []
green_pixels = []
blue_pixels = []

for r, g, b in image.get_flattened_data():
    red_pixels.append((r, 0, 0))
    green_pixels.append((0, g, 0))
    blue_pixels.append((0, 0, b))
red_image.putdata(red_pixels)
green_image.putdata(green_pixels)
blue_image.putdata(blue_pixels)

plt.figure(figsize = (12, 8))

plt.subplot(2, 2, 1)
plt.imshow(image)
plt.title("Original RGB Image")
plt.axis("off")

plt.subplot(2, 2, 2)
plt.imshow(red_image)
plt.title("Red Channel")
plt.axis("off")

plt.subplot(2, 2, 3)
plt.imshow(green_image)
plt.title("Green Channel")
plt.axis("off")

plt.subplot(2, 2, 4)
plt.imshow(blue_image)
plt.title("Blue Channel")
plt.axis("off")

plt.tight_layout()
plt.show()

red_image.save("Output/Task_02_Separate_RGB_Channels_Red_Channel.png")
green_image.save("Output/Task_02_Separate_RGB_Channels_Green_Channel.png")
blue_image.save("Output/Task_02_Separate_RGB_Channels_Blue_Channel.png")