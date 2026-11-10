from PIL import Image

image = Image.open('PNG/Task_01_RGB_to_Grayscale.png').convert('RGB')

width, height = image.size
gray_image = Image.new('L', (width, height))

for y in range(height):
    for x in range(width):
        r, g, b = image.getpixel((x, y))
        gray = int(0.299 * r + 0.587 * g + 0.114 * b)
        gray_image.putpixel((x, y), gray)

gray_image.save('Output/Task_01_RGB_to_Grayscale_gray.png')
print("Grayscale image saved as 'Output/Task_01_RGB_to_Grayscale_gray.png'")

