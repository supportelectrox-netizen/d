from PIL import Image

image = Image.open("PNG/Task_03_Image_Negative.png")

if image.mode != "L":
    raise ValueError("Image must be in grayscale mode (L)")

width, height = image.size
pixels = image.load()

for y in range(height):
    for x in range(width):
        original_pixels_intensity = pixels[x, y]
        negative_pixels_intensity = 255 - original_pixels_intensity
        pixels[x, y] = negative_pixels_intensity

image.save("Output/Task_03_Image_Negative_negative.png")
print("Negative image saved as 'Output/Task_03_Image_Negative_negative.png'")