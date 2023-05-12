from PIL import Image

# Open the image
image = Image.open('result/average_diff_image3.jpg')

# Get the pixel values
pixel_values = list(image.getdata())

# Print the pixel values
i = 0
for pixel in pixel_values:
    print(pixel, end=' ')

    if i % 1024==0:
        print()
        i += 1