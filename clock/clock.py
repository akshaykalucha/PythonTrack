import cv2
import numpy as np
from numpy.lib.type_check import imag
from utils import draw_time
from constants import colors, CANVAS_SIZE, radius
import utils

image = np.zeros(CANVAS_SIZE, dtype=np.uint8)
image[:] = [255,255,255]

init, final = utils.clock_dots_and_ticks()



for i in range(len(init)):
    if i % 5 == 0:
        cv2.line(image, init[i], final[i], colors['black'], 3)
    else:
        cv2.circle(image, init[i], 5, colors['gray'], -1)

cv2.circle(image, (320, 320), radius+10, colors['dark_red'], 2)

cv2.putText(image, "Cv2Clock", (190,230), cv2.FONT_HERSHEY_DUPLEX, 2, colors['dark_gray'], 1, cv2.LINE_AA)

while True:
    image_orig = image.copy()
    clock = draw_time(image_orig)
    cv2.imshow("analog clock", image_orig)

    if cv2.waitKey(1) == ord('q'):
        break

cv2.destroyAllWindows()