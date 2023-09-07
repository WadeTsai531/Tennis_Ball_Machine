import cv2
import time
from PIL import Image, ImageTk
from utils.yolo_with_plugins import TrtYOLO
from datetime import datetime
import pycuda.autoinit  # This is needed for initializing CUDA driver

video_path = '../Videos/Testing_video_1112/20221112_test_4.mp4'
trt_weights_path = '../Training_Process/Person_Training_yolov4-tiny-L3_288-1115_all/' \
                   'Person_Training_yolov4-tiny-L3_288-1115_all.trt'

video = cv2.VideoCapture(video_path)

COLORS = [(0, 255, 255), (255, 255, 0), (0, 255, 0), (255, 0, 0)]
with open("../Training_Process/Person_Training_yolov4-tiny-L3_1106_all/classes.txt", "r") as f:
    class_names = [cname.strip() for cname in f.readlines()]
trt_yolo = TrtYOLO(trt_weights_path, 1)

while cv2.waitKey(1) < 1:
    ret, frame = video.read()
    frame = cv2.resize(frame, (640, 480))
    if not ret:
        print('Break')
        break
    start_time = time.time()
    boxes, scores, classes = trt_yolo.detect(frame, 0.6)
    fps = 1 / (time.time() - start_time)
    for (class_id, score, box) in zip(classes, scores, boxes):
        class_id = int(class_id)
        color = COLORS[int(class_id) % len(COLORS)]
        label = "%s : %f" % (class_names[class_id], score)
        cv2.rectangle(frame, (box[0], box[1]), (box[2], box[3]), color, 2)
        cv2.putText(frame, label, (box[0], box[1] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)
    cv2.putText(frame, 'FPS: %.2f' % fps, (0, 25), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
    cv2.imshow('frame', frame)

video.release()
