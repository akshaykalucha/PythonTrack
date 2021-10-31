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


def biggest_contour(contours):
    biggest = np.array([])
    max_area = 0
    for i in contours:
        # Get the area and perimeter of contour
        area = cv2.contourArea(i)
        peri = cv2.arcLength(i, True)

        # Approximate the (closed) curve and get its points
        approx = cv2.approxPolyDP(i, 0.02 * peri, True)

        # If current contour is bigger than previous one, AND it is a rectangle
        if area > max_area and len(approx) == 4:
            biggest = approx
            max_area = area

    # Squeeze to 2D matrix: (4, 1, 2) -> (4, 2)
    # biggest = np.squeeze(biggest, axis=1)

    return biggest, max_area


def draw_rectangle(img, biggest, thickness):
    # Squeeze to 2D matrix: (4, 1, 2) -> (4, 2)
    biggest = np.squeeze(biggest, axis=1)

    cv2.line(img, (biggest[0][0], biggest[0][1]), (biggest[1][0], biggest[1][1]), (0, 255, 0), thickness)
    cv2.line(img, (biggest[0][0], biggest[0][1]), (biggest[2][0], biggest[2][1]), (0, 255, 0), thickness)
    cv2.line(img, (biggest[3][0], biggest[3][1]), (biggest[2][0], biggest[2][1]), (0, 255, 0), thickness)
    cv2.line(img, (biggest[3][0], biggest[3][1]), (biggest[1][0], biggest[1][1]), (0, 255, 0), thickness)

    return img


def reorder(points):

    # Squeeze to 2D matrix: (4, 1, 2) -> (4, 2)
    points = np.squeeze(points, axis=1)

    points_new = np.zeros((4, 1, 2), dtype=np.int32)

    # Add the x and y values of all 4 points
    add = points.sum(1)

    # First point, with smallest x and y coordinates
    points_new[0] = points[np.argmin(add)]

    # Last point, with largest x and y coordinates
    points_new[3] = points[np.argmax(add)]

    # Subtract the x and y values of all 4 points
    diff = np.diff(points, axis=1)

    points_new[1] = points[np.argmin(diff)]
    points_new[2] = points[np.argmax(diff)]

    return points_new