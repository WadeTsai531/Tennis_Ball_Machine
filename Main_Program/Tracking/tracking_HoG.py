import cv2
import numpy as np
import serial
import time

Serial_BaudRate = 9600
Serial_Port = 'COM3'

print('Connecting to device ...')
ser = serial.Serial()
ser.baudrate = Serial_BaudRate
ser.port = Serial_Port

ser.open()
print('Connect successful')

hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

cam = cv2.VideoCapture(1, cv2.CAP_DSHOW)

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

send_data = 'S/'
ser.write(send_data.encode('utf-8'))


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
    gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)

    boxes, weights = hog.detectMultiScale(frame, winStride=(8, 8))
    boxes = np.array([[x, y, x + w, y + h] for (x, y, w, h) in boxes])

    cv2.rectangle(frame,
                  (center[0] - xy_range, center[1] - xy_range),
                  (center[0] + xy_range, center[1] + xy_range), (0, 255, 0), 3)

    point_x, point_y = 0, 0
    for (xA, yA, xB, yB) in boxes:
        center_x = (xB - xA) // 2
        center_y = (yB - yA) // 2
        if (center[0] - xy_range) <= xA + center_x <= (center[0] + xy_range) and \
                (center[1] - xy_range) <= yA + center_y <= (center[1] + xy_range):
            cv2.rectangle(frame, (xA, yA), (xB, yB), (0, 255, 0), 3)
            cv2.circle(frame, (xA + center_x, yA + center_y), 5, (0, 255, 0), 5)
            point_x, point_y = xA + center_x, yA + center_y
            break
    if point_x != 0 and point_y != 0:
        gap = point_x - center[0]
        if gap > 40:
            if turn_right_flag:
                x_power = abs(gap) * multiplier + offset
                send_data = 'R' + str(int(x_power)) + '/'
                ser.write(send_data.encode('utf-8'))
                turn_right_flag = False
                print('Turn Right')
                time.sleep(0.001)
            if x_power != abs(gap) * multiplier + offset:
                x_power = abs(gap) * multiplier + offset
                send_data = 'R' + str(int(x_power)) + '/'
                ser.write(send_data.encode('utf-8'))
        else:
            if not turn_right_flag:
                send_data = 'S/'
                ser.write(send_data.encode('utf-8'))
                turn_right_flag = True
                print('Stop')
                time.sleep(0.001)

        if gap < -40:
            if turn_left_flag:
                x_power = abs(gap) * multiplier + offset
                send_data = 'L' + str(int(x_power)) + '/'
                ser.write(send_data.encode('utf-8'))
                turn_left_flag = False
                print('Turn Left')
                time.sleep(0.001)
            if x_power != abs(gap) * multiplier + offset:
                x_power = abs(gap) * multiplier + offset
                send_data = 'L' + str(int(x_power)) + '/'
                ser.write(send_data.encode('utf-8'))
        else:
            if not turn_left_flag:
                send_data = 'S/'
                ser.write(send_data.encode('utf-8'))
                turn_left_flag = True
                print('Stop')
                time.sleep(0.001)
    else:
        if not turn_right_flag:
            send_data = 'S/'
            ser.write(send_data.encode('utf-8'))
            turn_right_flag = True
            print('Stop')
            time.sleep(0.001)

    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        send_data = 'S/'
        ser.write(send_data.encode('utf-8'))
        break

cam.release()
cv2.destroyAllWindows()
