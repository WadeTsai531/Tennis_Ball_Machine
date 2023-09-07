import cv2
import os


class Main:
    def __init__(self):
        self.image_path = '../../Dataset/Pos_Training_1125'
        self.video_path = '../../Videos/Pos_test_video_1125/IMG_3203-1.MOV'

        self.threshold = 20
        self.CONFIDENCE_THRESHOLD = 0.7
        self.NMS_THRESHOLD = 0.5
        self.COLORS = [(0, 255, 255), (255, 255, 0), (0, 255, 0), (255, 0, 0)]

        # -------- Load Config / Weights --------
        with open("../../Training_Process/COCO_Data/classes.txt", "r") as f:
            self.class_names = [cname.strip() for cname in f.readlines()]
        # config_path = '../../Training_Process/Person_Training_yolov4-tiny-L3_1108_without_coco/' \
        #               'Training_Person_yolov4-tiny-L3_1108_without_coco.cfg'
        # weights_path = '../../Training_Process/Person_Training_yolov4-tiny-L3_1108_without_coco/' \
        #                'Training_Person_yolov4-tiny-L3_1108_without_coco_final.weights'

        weights_path = '../../Training_Process/COCO_Data/yolov4.cfg'
        config_path = '../../Training_Process/COCO_Data/yolov4.weights'

        # -------- OpenCV Loading Yolov4 --------
        net = cv2.dnn.readNet(weights_path, config_path)
        net.setPreferableBackend(cv2.dnn.DNN_BACKEND_CUDA)
        net.setPreferableTarget(cv2.dnn.DNN_TARGET_CUDA)
        self.model = cv2.dnn_DetectionModel(net)
        self.model.setInputParams(size=(416, 416), scale=1 / 255, swapRB=True)

        self.Detect_video()

    def Detect_video(self):
        print('Start Detect')
        coordinate = None
        image_count = 1
        video = cv2.VideoCapture(self.video_path)
        while cv2.waitKey(1) < 1:
            ret, frame = video.read()
            if not ret:
                print('Over')
                break

            # frame = cv2.resize(frame, (0, 0), 0, 0.6, 0.6)
            frame_copy = frame.copy()
            h, w = frame.shape[:2]
            data_list = []
            write_txt_flag = False

            classes, scores, boxes = self.model.detect(frame_copy,
                                                       self.CONFIDENCE_THRESHOLD,
                                                       self.NMS_THRESHOLD)
            for (class_id, score, box) in zip(classes, scores, boxes):
                color = self.COLORS[int(class_id) % len(self.COLORS)]
                label = "%s : %f" % (self.class_names[class_id], score)
                if class_id == 0:
                    write_txt_flag = True
                    x_min = box[0]
                    y_min = box[1]
                    yolo_w = box[2]
                    yolo_h = box[3]

                    x_center = (x_min + x_min + yolo_w) // 2
                    y_center = (y_min + y_min + yolo_h) // 2

                    print('x_min: {}, '
                          'y_min: {}, '
                          'yolo_w: {}, '
                          'yolo_h: {}, '
                          'x_center: {}, '
                          'y_center: {}'.format(
                        x_min, y_min, yolo_w, yolo_h, x_center, y_center))
                    data_list.append([x_center / w,
                                      y_center / h,
                                      yolo_w / w,
                                      yolo_h / h])
                    cv2.circle(frame_copy, (x_center, y_center), 2, (0, 0, 255), 3)
                    cv2.rectangle(frame_copy, box, color, 2)
                    cv2.putText(frame_copy, label, (box[0], box[1] - 10),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)

            if write_txt_flag:
                if coordinate is None:
                    coordinate = int(data_list[0][0] * w)
                    image_name = str(image_count) + '.jpg'
                    cv2.imwrite(os.path.join(self.image_path, image_name), frame)
                    print('Save Image: {}'.format(
                        os.path.join(self.image_path, image_name)))
                    image_count += 1
                    self.Write_txt(self.image_path, image_name, data_list)
                else:
                    if abs(int(data_list[0][0] * w) - coordinate) >= self.threshold:
                        coordinate = int(data_list[0][0] * w)
                        image_name = str(image_count) + '.jpg'
                        cv2.imwrite(os.path.join(self.image_path, image_name), frame)
                        print('Save Image: {}'.format(
                            os.path.join(self.image_path, image_name)))
                        image_count += 1
                        self.Write_txt(self.image_path, image_name, data_list)
            cv2.imshow('frame', frame_copy)

    def Write_txt(self, save_path, image_name, data_list):
        print('Write Txt File')
        with open(os.path.join(save_path, image_name.replace('.jpg', '.txt')), 'w') as data:
            for bbox in data_list:
                form = str(0) + ' ' + \
                       str(bbox[0]) + ' ' + str(bbox[1]) + ' ' + \
                       str(bbox[2]) + ' ' + str(bbox[3])
                data.write(form + '\n')


Main()
