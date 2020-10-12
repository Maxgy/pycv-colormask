#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    low_green = np.array([30, 100, 100])
    up_green = np.array([60, 255, 255])

    low_cyan = np.array([60, 100, 100])
    up_cyan = np.array([90, 255, 255])

    low_blue = np.array([90, 100, 100])
    up_blue = np.array([120, 255, 255])

    low_purple = np.array([120, 100, 100])
    up_purple = np.array([150, 255, 255])

    low_red = np.array([150, 100, 100])
    up_red = np.array([180, 255, 255])

    low_yellow = np.array([10, 100, 100])
    up_yellow = np.array([30, 255, 255])

    green_mask = cv2.inRange(hsv, low_green, up_green)
    cyan_mask = cv2.inRange(hsv, low_cyan, up_cyan)
    blue_mask = cv2.inRange(hsv, low_blue, up_blue)
    purple_mask = cv2.inRange(hsv, low_purple, up_purple)
    red_mask = cv2.inRange(hsv, low_red, up_red)
    yellow_mask = cv2.inRange(hsv, low_yellow, up_yellow)

    green_res = cv2.bitwise_and(frame, frame, mask=green_mask)
    cyan_res = cv2.bitwise_and(frame, frame, mask=cyan_mask)
    blue_res = cv2.bitwise_and(frame, frame, mask=blue_mask)
    purple_res = cv2.bitwise_and(frame, frame, mask=purple_mask)
    red_res = cv2.bitwise_and(frame, frame, mask=red_mask)
    yellow_res = cv2.bitwise_and(frame, frame, mask=yellow_mask)

    print(1.0 * blue_res.sum() / 1.e6)
    print(hsv)

    cv2.imshow("frame", frame)
    if len(sys.argv) > 1:
        color = sys.argv[1]
        if color == "green":
            cv2.imshow(color, green_res)
        elif color == "cyan":
            cv2.imshow(color, cyan_res)
        elif color == "blue":
            cv2.imshow(color, blue_res)
        elif color == "purple":
            cv2.imshow(color, purple_res)
        elif color == "red":
            cv2.imshow(color, red_res)
        elif color == "yellow":
            cv2.imshow(color, yellow_res)
    else:
        cv2.imshow("green", green_res)
        cv2.imshow("cyan", cyan_res)
        cv2.imshow("blue", blue_res)
        cv2.imshow("purple", purple_res)
        cv2.imshow("red", red_res)
        cv2.imshow("yellow", yellow_res)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
