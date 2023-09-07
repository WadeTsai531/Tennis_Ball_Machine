import cv2
from utils.yolo_with_plugins import TrtYOLO
import pycuda.autoinit  # This is needed for initializing CUDA driver


class Main:
    model_path = '../Training_Process/Person_Training_yolov4-tiny-288_1114/' \
                 'Person_Training_yolov4-tiny-288_1114.trt'
    video_path = '../Videos/Testing_video_1112/20221112_test_4.mp4'

    def __init__(self):
        gst_str = ('v4l2src device=/dev/video{} ! '
                   'video/x-raw, width=(int){}, height=(int){} ! '
                   'videoconvert ! appsink').format(0, 640, 480)
        self.cam = cv2.VideoCapture(self.video_path)

        # -------- Yolov4 Setup --------
        self.center = [int(640) // 2, int(480) // 2]
        self.xy_range = [150, 100]
        self.COLORS = [(0, 255, 255), (255, 255, 0), (0, 255, 0), (255, 0, 0)]
        with open("../Training_Process/Person_Training_yolov4-tiny-288_1114/classes.txt", "r") as f:
            self.class_names = [cname.strip() for cname in f.readlines()]
        self.trt_yolo = TrtYOLO(self.model_path, 1)

        while cv2.waitKey(30) < 1:
            ret, frame = self.cam.read()
            if not ret:
                print('Bleak')
                break
            frame = cv2.resize(frame, (640, 480))
            result_frame = self.Tracking(frame)
            cv2.imshow('frame', result_frame)
        self.cam.release()

    def Tracking(self, frame):
        boxes, scores, classes = self.trt_yolo.detect(frame, 0.6)
        cv2.line(frame, (320 - self.xy_range[0], 0), (320 - self.xy_range[0], 480), (255, 0, 0), 2)
        cv2.line(frame, (320 + self.xy_range[0], 0), (320 + self.xy_range[0], 480), (255, 0, 0), 2)

        point_x, point_y = 0, 0
        x_min = y_min = x_max = y_max = 0
        for (class_id, score, box) in zip(classes, scores, boxes):
            class_id = int(class_id)
            color = self.COLORS[int(class_id) % len(self.COLORS)]
            label = "%s : %f" % (self.class_names[class_id], score)
            if class_id == 0:
                x_min, y_min, x_max, y_max = box
                x_center = (x_max + x_min) // 2
                y_center = (y_max + y_min) // 2
                if (self.center[0] - self.xy_range[0]) <= x_center <= (self.center[0] + self.xy_range[0]) and \
                        (self.center[1] - self.xy_range[1]) <= y_center <= (self.center[1] + self.xy_range[1]) or True:
                    point_x, point_y = x_center, y_center
                    cv2.circle(frame, (x_center, y_center), 2, (0, 255, 0), 4)
                    cv2.rectangle(frame, (box[0], box[1]), (box[2], box[3]), color, 2)
                    cv2.putText(frame, label, (box[0], box[1] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)

        if point_x != 0 and point_y != 0:
            gap = point_x - self.center[0]
            if gap < -80:
                status = 'Right'
            elif gap > 80:
                status = 'Left'
            else:
                status = 'Stop'
            size = round((x_max - x_min) * (y_max - y_min) / 1000, 1)
            scale = 4
            offset = 40
            cv2.line(frame, (320 - int(size * scale) - offset, y_min),
                     (320 - int(size * scale) - offset, y_max), (0, 0, 255), 2)
            cv2.line(frame, (320 + int(size * scale) + offset, y_min),
                     (320 + int(size * scale) + offset, y_max), (0, 0, 255), 2)
            print('Point-x: {} Point-y: {} - Status: {} Gap: {} Size: {}'.format(point_x, point_y, status, gap, size))

        return frame


Main()
