import cv2
import math
import datetime
from constants import colors
from constants import radius
from constants import center

def clock_dots_and_ticks():
    initial = []
    final = []
    for i in range(0,360,6):
        x_cordinate = int(center[0] + radius * math.cos(i*math.pi/180))
        y_cordinate = int(center[1] + radius * math.sin(i*math.pi/180))

        initial.append((x_cordinate, y_cordinate))

    for i in range(0,360,6):
        x_cordinate = int(center[0] + (radius - 20) * math.cos(i*math.pi/180))
        y_cordinate = int(center[1] + (radius - 20) * math.sin(i*math.pi/180))

        final.append((x_cordinate, y_cordinate))
    return initial, final

def getTime(h,m,s):
    time = ""
    hour = ""
    minute = ""
    second = ""
    if h < 10:
        hour = f"0{h}"
    else:
        hour = f"{h}"
    if m < 10:
        minute = f"0{m}"
    else:
        minute = f"{m}"
    if s < 10:
        second = f"0{s}"
    else:
        second = f"{s}"
    time = f"{hour}:{minute}:{second}"
    return time


def draw_time(img):
    time_now = datetime.datetime.now().time()
    hour = math.fmod(time_now.hour, 12)
    minute = time_now.minute
    second = time_now.second

    second_angle = math.fmod(second * 6 + 270, 360)
    minute_angle = math.fmod(minute * 6 + 270, 360)
    hour_angle = math.fmod((hour*30) + (minute/2) + 270, 360)

    second_x = int(center[0] + (radius-15) * math.cos(second_angle*math.pi/180))
    second_y = int(center[1] + (radius-15) * math.sin(second_angle*math.pi/180))
    cv2.line(img, center, (second_x, second_y), colors['black'], 2)

    minute_x = int(center[0] + (radius-50) * math.cos(minute_angle*math.pi/180))
    minute_y = int(center[1] + (radius-15) * math.sin(minute_angle*math.pi/180))
    cv2.line(img, center, (minute_x, minute_y), colors['amber'], 3)

    hour_x = int(center[0] + (radius-90) * math.cos(hour_angle*math.pi/180))
    hour_y = int(center[1] + (radius-90) * math.sin(hour_angle*math.pi/180))
    cv2.line(img, center, (hour_x, hour_y), colors['amber'], 3)

    cv2.circle(img, center, 5, colors['dark_gray'], -1)

    time = getTime(int(hour), minute, second)

    cv2.putText(img, time, (200,300), cv2.FONT_HERSHEY_DUPLEX, 1.6, colors['red'], 1, cv2.LINE_AA)

    return img