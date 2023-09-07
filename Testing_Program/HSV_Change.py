import cv2
import numpy as np


def on_Change(x):
    pass


image = cv2.imread('../Dataset/Person_Training_0914/001.jpg')
image = cv2.resize(image, None, fx=0.5, fy=0.5)
image_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

cv2.namedWindow('Scale Window')
cv2.createTrackbar('H Min', 'Scale Window', 0, 179, on_Change)
cv2.createTrackbar('H Max', 'Scale Window', 10, 179, on_Change)
cv2.createTrackbar('S Min', 'Scale Window', 0, 255, on_Change)
cv2.createTrackbar('S Max', 'Scale Window', 10, 255, on_Change)
cv2.createTrackbar('V Min', 'Scale Window', 245, 255, on_Change)
cv2.createTrackbar('V Max', 'Scale Window', 247, 255, on_Change)

while True:
    h_min = cv2.getTrackbarPos('H Min', 'Scale Window')
    h_max = cv2.getTrackbarPos('H Max', 'Scale Window')
    s_min = cv2.getTrackbarPos('S Min', 'Scale Window')
    s_max = cv2.getTrackbarPos('S Max', 'Scale Window')
    v_min = cv2.getTrackbarPos('V Min', 'Scale Window')
    v_max = cv2.getTrackbarPos('V Max', 'Scale Window')
    # HSV_Data = [[h_min, s_min, v_min], [h_max, s_max, v_max]]

    lower = np.array([h_min, s_min, v_min])
    upper = np.array([h_max, s_max, v_max])

    mask = cv2.inRange(image_hsv, lower, upper)
    r = cv2.bitwise_and(image_hsv, image_hsv, mask=mask)
    # image_hsv = cv2.bitwise_not(mask)

    cv2.imshow('HSV Image', r)
    if cv2.waitKey(1) == ord('q'):
        break
