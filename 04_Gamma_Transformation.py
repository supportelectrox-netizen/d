from PIL import Image

image = Image.open("PNG/Task_04_Gamma_Transformation.png")

if image.mode not in ("L", "RGB"):
    image = image.convert("RGB")

width, height = image.size

gamma = [0.5, 1.0, 2.0]

for g in gamma:
    if g <= 0:
        raise ValueError("Gamma value must be greater than 0")

    output_image = Image.new(image.mode, (width, height))

    input_pixels = image.load()
    output_pixels = output_image.load()

    for y in range(height):
        for x in range(width):
            pixel = input_pixels[x, y]
            if image.mode == "L":
                new_pixel = int(255 * (pixel / 255) ** g)
                output_pixels[x, y] = new_pixel
            else:
                r, g, b = pixel
                new_r = int(255 * (r / 255) ** g)
                new_g = int(255 * (g / 255) ** g)
                new_b = int(255 * (b / 255) ** g)
                output_pixels[x, y] = (new_r, new_g, new_b)
    output_image.save(f"Output/Task_04_Gamma_Transformation_gamma_{g}.png")
    print(f"Gamma transformed image saved as 'Output/Task_04_Gamma_Transformation_gamma_{g}.png'")
