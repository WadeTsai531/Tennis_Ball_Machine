import time
import cv2

CONFIDENCE_THRESHOLD = 0.5
NMS_THRESHOLD = 0.4
COLORS = [(0, 255, 255), (255, 255, 0), (0, 255, 0), (255, 0, 0)]

with open("../Training_Process/COCO_Data/classes.txt", "r") as f:
    class_names = [cname.strip() for cname in f.readlines()]

# weights_path = '../Training_Process/Person_Training_yolov4-tiny-L3_288-1115_all/' \
#                  'Person_Training_yolov4-tiny-L3_288-1115_all.weights'
# config_path = '../Training_Process/Person_Training_yolov4-tiny-L3_288-1115_all/' \
#                   'Person_Training_yolov4-tiny-L3_288-1115_all.cfg'

weights_path = '../Training_Process/COCO_Data/yolov4.cfg'
config_path = '../Training_Process/COCO_Data/yolov4.weights'
net = cv2.dnn.readNet(weights_path, config_path)
net.setPreferableBackend(cv2.dnn.DNN_BACKEND_CUDA)
net.setPreferableTarget(cv2.dnn.DNN_TARGET_CUDA)

model = cv2.dnn_DetectionModel(net)
model.setInputParams(size=(608, 608), scale=1 / 255, swapRB=True)

video_path = '../Videos/Video_from_Web/test_v2.mp4'
video = cv2.VideoCapture(video_path)

while cv2.waitKey(1) < 1:
    ret, frame = video.read()
    if not ret:
        print('Break')
        break
    # frame = cv2.resize(frame, (640, 480))
    start = time.time()
    classes, scores, boxes = model.detect(frame, CONFIDENCE_THRESHOLD, NMS_THRESHOLD)
    end = time.time()

    start_drawing = time.time()
    for (classid, score, box) in zip(classes, scores, boxes):
        color = COLORS[int(classid) % len(COLORS)]
        label = "%s : %f" % (class_names[classid[0]], score)
        cv2.rectangle(frame, box, color, 2)
        cv2.putText(frame, label, (box[0], box[1] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)
    end_drawing = time.time()

    fps_label = "FPS: %.2f" % (1 / (end - start))
    cv2.putText(frame, fps_label, (0, 25), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
    cv2.imshow("detections", frame)
