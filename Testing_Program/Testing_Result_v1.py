import cv2
import os
import time


class Main:
    CONFIDENCE_THRESHOLD = 0.4
    model_path = '../Training_Process/Person_Training_yolov4-tiny-L3_288-1115_all/' \
                 'Person_Training_yolov4-tiny-L3_288-1115_all.weights'
    config_path = '../Training_Process/Person_Training_yolov4-tiny-L3_288-1115_all/' \
                  'Person_Training_yolov4-tiny-L3_288-1115_all.cfg'
    video_path = '../Videos/Testing_video_1120/Tracking.mp4'
    save_path = '../Videos/Testing_video_1120_Result/Tracking-Result-1120_3.mp4'

    def __init__(self):
        self.Yolov4_setup()
        self.video = cv2.VideoCapture(self.video_path)
        fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
        out = cv2.VideoWriter(self.save_path, fourcc, 30, (640, 480))
        while cv2.waitKey(5) < 1:
            ret, frame = self.video.read()
            if not ret:
                print('Over')
                break
            frame = cv2.resize(frame, (640, 480))
            frame = self.Tracking(frame)
            out.write(frame)
            cv2.imshow('frame', frame)
        self.video.release()
        out.release()

    def Yolov4_setup(self):
        # -------- Yolov4 Setup --------
        self.center = [int(640) // 2, int(480) // 2]
        self.xy_range = [150, 100]
        self.COLORS = [(0, 255, 255), (255, 255, 0), (0, 255, 0), (255, 0, 0)]
        with open("./classes.txt", "r") as f:
            self.class_names = [cname.strip() for cname in f.readlines()]
        # self.trt_yolo = TrtYOLO(self.model_path, 1)

        self.NMS_THRESHOLD = 0.5
        net = cv2.dnn.readNet(self.model_path, self.config_path)
        net.setPreferableBackend(cv2.dnn.DNN_BACKEND_CUDA)
        net.setPreferableTarget(cv2.dnn.DNN_TARGET_CUDA)
        self.model = cv2.dnn_DetectionModel(net)
        self.model.setInputParams(size=(288, 288), scale=1 / 255, swapRB=True)

    def Tracking(self, frame):
        # boxes, scores, classes = self.trt_yolo.detect(frame, 0.4)
        classes, scores, boxes = self.model.detect(frame, self.CONFIDENCE_THRESHOLD, self.NMS_THRESHOLD)
        cv2.line(frame, (320 - self.xy_range[0], 0), (320 - self.xy_range[0], 480), (255, 0, 0), 2)
        cv2.line(frame, (320 + self.xy_range[0], 0), (320 + self.xy_range[0], 480), (255, 0, 0), 2)

        cv2.line(frame, (320 - 70, 200), (320 - 70, 400), (0, 0, 255), 2)
        cv2.line(frame, (320 + 70, 200), (320 + 70, 400), (0, 0, 255), 2)

        point_x, point_y = 0, 0
        x_min, y_min, x_max, y_max = 0, 0, 0, 0
        for (class_id, score, box) in zip(classes, scores, boxes):
            class_id = int(class_id)
            color = self.COLORS[int(class_id) % len(self.COLORS)]
            label = "%s : %f" % (self.class_names[class_id], score)
            if class_id == 0:
                # ---- trt ----
                # x_min, y_min, x_max, y_max = box

                # ---- opencv ----
                x_min, y_min, w, h = box
                x_max = x_min + w
                y_max = y_min + h

                x_center = (x_max + x_min) // 2
                y_center = (y_max + y_min) // 2
                if (self.center[0] - self.xy_range[0]) <= x_center <= (self.center[0] + self.xy_range[0]) and \
                        (self.center[1] - self.xy_range[1]) <= y_center <= (self.center[1] + self.xy_range[1]):
                    point_x, point_y = x_center, y_center
                    cv2.circle(frame, (x_center, y_center), 5, (0, 255, 0), 5)
                    cv2.rectangle(frame, (x_min, y_min), (x_max, y_max), color, 2)
                    cv2.putText(frame, label, (box[0], box[1] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)
        return frame


Main()
