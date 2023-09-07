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

cam = cv2.VideoCapture(1)

cam_width = cam.get(cv2.CAP_PROP_FRAME_WIDTH)
cam_height = cam.get(cv2.CAP_PROP_FRAME_HEIGHT)
center = [cam_width // 2, cam_height // 2]

turn_right_flag = True
turn_left_flag = True

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

    '''for (xA, yA, xB, yB) in boxes:
        # display the detected boxes in the colour picture
        cv2.rectangle(frame, (xA, yA), (xB, yB), (0, 255, 0), 2)'''
    if len(boxes) == 1:
        xA, yA, xB, yB = boxes[0]
        cv2.rectangle(frame, (xA, yA), (xB, yB), (0, 255, 0), 2)
        now_center = (xA + xB) // 2

        # print(now_center - center[0], end=', ')
        if (now_center - center[0]) > 80:
            if turn_right_flag:
                send_data = 'L/'
                ser.write(send_data.encode('utf-8'))
                turn_right_flag = False
                print('Turn Right')
                time.sleep(0.001)
        else:
            if not turn_right_flag:
                send_data = 'S/'
                ser.write(send_data.encode('utf-8'))
                turn_right_flag = True
                print('Stop')
                time.sleep(0.001)

        if (now_center - center[0]) < -80:
            if turn_left_flag:
                send_data = 'R/'
                ser.write(send_data.encode('utf-8'))
                turn_left_flag = False
                print('Turn Left')
                time.sleep(0.001)
        else:
            if not turn_left_flag:
                send_data = 'S/'
                ser.write(send_data.encode('utf-8'))
                turn_left_flag = True
                print('Stop')
                time.sleep(0.001)

    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        send_data = 'S/'
        ser.write(send_data.encode('utf-8'))
        break

cam.release()
cv2.destroyAllWindows()
