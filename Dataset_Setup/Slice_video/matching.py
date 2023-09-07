import os
import cv2
import numpy as np

temple = cv2.imread('1.jpg')
image = cv2.imread('1.jpg')
threshold = 0.5
result = cv2.matchTemplate(image, temple, cv2.TM_CCOEFF_NORMED)
print(result[0][0])
