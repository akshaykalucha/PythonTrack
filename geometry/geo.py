import numpy as np
import cv2

# animate geometric designs for kids

canvas = np.zeros((840,840,3), dtype=np.uint8)
canvas[:] = [255, 255, 255]
start = 100
height, width, c = canvas.shape
fourcc = cv2.VideoWriter_fourcc(*'MJPG')
fps = 30
out = cv2.VideoWriter('shape.avi', fourcc, fps, (height, width))

while start != 391:
    canvas = cv2.rectangle(canvas, (start,10), (390,200), (0,0,0), 2, cv2.LINE_4)
    
    out.write(canvas)
    start += 1

out.release()
cv2.imshow('ss', canvas)
cv2.waitKey(0)