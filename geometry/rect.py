import cv2
import numpy as np


canvas = np.zeros((840,840,3), dtype=np.uint8)
canvas[:] = [255, 255, 255]

height, width, c = canvas.shape
fourcc = cv2.VideoWriter_fourcc(*'MJPG')
fps = 30
out = cv2.VideoWriter('rect.avi', fourcc, fps, (width, height))

beg = 100
end = (700, 250)


while beg != 700:
    canvas = cv2.rectangle(canvas, (beg, 10), end, (0,0,0), 1)
    beg += 1

    out.write(canvas)

out.release()
