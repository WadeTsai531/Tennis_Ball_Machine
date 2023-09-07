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

CONFIDENCE_THRESHOLD = 0.2
NMS_THRESHOLD = 0.4
COLORS = [(0, 255, 255), (255, 255, 0), (0, 255, 0), (255, 0, 0)]

with open("../../Training_Process/coco_test/classes.txt", "r") as f:
    class_names = [cname.strip() for cname in f.readlines()]
config_path = '../../Training_Process/0331_training(tiny)/yolov4.cfg'
weights_path = '../../Training_Process/0331_training(tiny)/weight/yolov4-custom_final.weights'

net = cv2.dnn.readNet(weights_path, config_path)
net.setPreferableBackend(cv2.dnn.DNN_BACKEND_CUDA)
net.setPreferableTarget(cv2.dnn.DNN_TARGET_CUDA)

model = cv2.dnn_DetectionModel(net)
model.setInputParams(size=(320, 320), scale=1 / 255, swapRB=True)

cam = cv2.VideoCapture(1, cv2.CAP_DSHOW)

cam_width = int(cam.get(cv2.CAP_PROP_FRAME_WIDTH))
cam_height = int(cam.get(cv2.CAP_PROP_FRAME_HEIGHT))
center = [cam_width // 2, cam_height // 2]
xy_range = 150

print(cam_width, cam_height)

turn_right_flag = True
turn_left_flag = True
x_power = 0
multiplier = 1
offset = 210

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
    # gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
    classes, scores, boxes = model.detect(frame, CONFIDENCE_THRESHOLD, NMS_THRESHOLD)
    cv2.rectangle(frame,
                  (center[0] - xy_range, center[1] - xy_range + 50),
                  (center[0] + xy_range, center[1] + xy_range + 70), (0, 255, 0), 3)

    point_x, point_y = 0, 0
    for (classid, score, box) in zip(classes, scores, boxes):
        color = COLORS[int(classid) % len(COLORS)]
        label = "%s : %f" % (class_names[classid[0]], score)
        if classid == 0:
            x_min, y_min, w, h = box
            x_max = x_min + w
            y_max = y_min + h

            x_center = (x_max + x_min) // 2
            y_center = (y_max + y_min) // 2

            if (center[0] - xy_range) <= x_center <= (center[0] + xy_range) and \
                    (center[1] - xy_range) <= y_center <= (center[1] + xy_range):
                point_x, point_y = x_center, y_center
                cv2.circle(frame, (x_center, y_center), 5, (0, 255, 0), 5)
                cv2.rectangle(frame, box, color, 2)
                cv2.putText(frame, label, (box[0], box[1] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)

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
