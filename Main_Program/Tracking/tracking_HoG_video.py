import cv2
import numpy as np

hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

# cam = cv2.VideoCapture(1, cv2.CAP_DSHOW)
cam = cv2.VideoCapture('../Training_Process/test_v5.mp4')

cam_width = int(cam.get(cv2.CAP_PROP_FRAME_WIDTH))
cam_height = int(cam.get(cv2.CAP_PROP_FRAME_HEIGHT))
center = [cam_width // 2, cam_height // 2]
xy_range = 100

print(cam_width, cam_height)

turn_right_flag = True
turn_left_flag = True
x_power = 0
multiplier = 1
offset = 150


def transform(data_in):
    if data_in >= 100:
        data_send = str(data_in)
    elif 100 > data_in >= 10:
        data_send = '0' + str(data_in)
    else:
        data_send = '00' + str(data_in)
    return data_send


while True:
    ret, frame = cam.read()
    frame = cv2.resize(frame, (0, 0), 0, 0.5, 0.5)
    gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)

    boxes, weights = hog.detectMultiScale(gray, winStride=(8, 8))
    boxes = np.array([[x, y, x + w, y + h] for (x, y, w, h) in boxes])

    for (xA, yA, xB, yB) in boxes:
        center_x = (xB - xA) // 2
        center_y = (yB - yA) // 2
        cv2.rectangle(frame, (xA, yA), (xB, yB), (0, 255, 0), 3)

    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()
