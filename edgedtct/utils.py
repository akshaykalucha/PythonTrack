import cv2
import PIL.Image as Image
import numpy as np

IMAGES_PATH = "./img/"

ROWS = 2
COLUMNS = 4
IMAGE_SAVE_PATH = './img/final.png'
height = 1280
width = 962

# Define image stitching function
def image_grid(image_names, IMAGE_SIZE_C, IMAGE_SIZE_R):
    # Create a new canvas on which all the images would be placed
    to_image = Image.new('RGBA', (COLUMNS * IMAGE_SIZE_C, ROWS * IMAGE_SIZE_R))
    # Loop through all pictures, paste each picture
    for y in range(0, ROWS):
        for x in range(0, COLUMNS):
            from_image = image_names[y * COLUMNS + x]
            to_image.paste(Image.fromarray(from_image), (x * IMAGE_SIZE_C, y * IMAGE_SIZE_R))

    to_image.save("./img/pipeline.png")
    return to_image