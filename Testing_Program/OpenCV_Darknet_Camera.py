import time
import cv2

CONFIDENCE_THRESHOLD = 0.4
NMS_THRESHOLD = 0.5
COLORS = [(0, 255, 255), (255, 255, 0), (0, 255, 0), (255, 0, 0)]

with open("../Training_Process/Person_Training_yolov4-tiny-L3_1106_all/classes.txt", "r") as f:
    class_names = [cname.strip() for cname in f.readlines()]
config_path = '../Training_Process/Person_Training_yolov4-tiny-L3_1108_without_coco/' \
              'Training_Person_yolov4-tiny-L3_1108_without_coco.cfg'
weights_path = '../Training_Process/Person_Training_yolov4-tiny-L3_1108_without_coco/' \
               'Training_Person_yolov4-tiny-L3_1108_without_coco_final.weights'

# net = cv2.dnn.readNetFromDarknet(config_path, weights_path)
net = cv2.dnn.readNet(weights_path, config_path)
net.setPreferableBackend(cv2.dnn.DNN_BACKEND_CUDA)
net.setPreferableTarget(cv2.dnn.DNN_TARGET_CUDA)

model = cv2.dnn_DetectionModel(net)
model.setInputParams(size=(416, 416), scale=1 / 255, swapRB=True)

gst_str = ('v4l2src device=/dev/video{} ! '
           'video/x-raw, width=(int){}, height=(int){} ! '
           'videoconvert ! appsink').format(0, 640, 480)
cam = cv2.VideoCapture(gst_str, cv2.CAP_GSTREAMER)

while cv2.waitKey(1) < 1:
    ret, frame = cam.read()
    if not ret:
        print('Break')
        break
    # frame = cv2.resize(frame, (0, 0), 0, 0.5, 0.5)
    start = time.time()
    classes, scores, boxes = model.detect(frame, CONFIDENCE_THRESHOLD, NMS_THRESHOLD)
    end = time.time()

    start_drawing = time.time()
    for (classid, score, box) in zip(classes, scores, boxes):
        color = COLORS[int(classid) % len(COLORS)]
        label = "%s : %f" % (class_names[classid], score)
        if classid == 0 or True:
            cv2.rectangle(frame, box, color, 2)
            cv2.putText(frame, label, (box[0], box[1] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)
            xA, yA, xB, yB = box
            print(xA, yA, xB, yB)
    end_drawing = time.time()

    fps_label = "FPS: %.2f (excluding drawing time of %.2fms)" % (
        1 / (end - start), (end_drawing - start_drawing) * 1000)
    cv2.putText(frame, fps_label, (0, 25), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
    cv2.imshow("detections", frame)
