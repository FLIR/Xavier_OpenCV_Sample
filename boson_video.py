#!/usr/bin/python3

import cv2
import numpy as np
import matplotlib.pyplot as plt

vid = cv2.VideoCapture(0)
vid.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'RGGB'))
vid.set(cv2.CAP_PROP_CONVERT_RGB, False)

while vid.isOpened():
    empty, frame = vid.read()

    cv2.imshow("s", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

vid.release()
print('done')
