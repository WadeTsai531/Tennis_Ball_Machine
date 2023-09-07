import os
import cv2


def Capture_From_Video(vid_path, video_index, image_path, txt_path):
    # -------- Video Split Variable --------
    frame_count = 0
    cap_temple = None
    threshold = 0.93

    # -------- Build Image Save Folder --------
    if not os.path.isdir(image_path):
        os.mkdir(image_path)

    video = cv2.VideoCapture(vid_path)
    while cv2.waitKey(1) < 1:
        ret, frame = video.read()
        if not ret:
            print('Over')
            break

        frame = cv2.resize(frame, (0, 0), 0, 0.8, 0.8)
        frame_copy = frame.copy()
        image_name = ''
        write_txt_flag = False
        if cap_temple is None:
            write_txt_flag = True
            cap_temple = frame.copy()
            image_name = str(video_index) + '-' + str(frame_count) + '.jpg'
            cv2.imwrite(os.path.join(image_path, str(video_index) + '-' + str(frame_count) + '.jpg'), frame)
            print('Save Image: {}'.format(
                os.path.join(image_path, str(video_index) + '-' + str(frame_count) + '.jpg')))
            frame_count += 1
        else:
            result = cv2.matchTemplate(frame, cap_temple, cv2.TM_CCOEFF_NORMED)
            result = round(result[0][0], 3)
            if result <= threshold:
                write_txt_flag = True
                cap_temple = frame.copy()
                image_name = str(video_index) + '-' + str(frame_count) + '.jpg'
                cv2.imwrite(os.path.join(image_path, str(video_index) + '-' + str(frame_count) + '.jpg'), frame)
                print('Save Image: {} --- Result: {}'.format(
                    os.path.join(image_path, str(video_index) + '-' + str(frame_count) + '.jpg'), result))
                frame_count += 1

        # -------- Detect Frame --------
        data_list = []
        h, w = frame.shape[:2]
        classes, scores, boxes = model.detect(frame_copy, CONFIDENCE_THRESHOLD, NMS_THRESHOLD)
        for (class_id, score, box) in zip(classes, scores, boxes):
            color = COLORS[int(class_id) % len(COLORS)]
            label = "%s : %f" % (class_names[class_id[0]], score)
            if class_id == 0:
                x_min = box[0]
                y_min = box[1]
                yolo_w = box[2]
                yolo_h = box[3]

                x_center = (x_min + x_min + yolo_w) // 2
                y_center = (y_min + y_min + yolo_h) // 2

                print('x_min: {}, y_min: {}, yolo_w: {}, yolo_h: {}, x_center: {}, y_center: {}'.format(
                    x_min, y_min, yolo_w, yolo_h, x_center, y_center))
                data_list.append([x_center / w,
                                  y_center / h,
                                  yolo_w / w,
                                  yolo_h / h])
                cv2.circle(frame_copy, (x_center, y_center), 2, (0, 0, 255), 3)
                cv2.rectangle(frame_copy, box, color, 2)
                cv2.putText(frame_copy, label, (box[0], box[1] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)

        if write_txt_flag:
            print('Write Txt File')
            with open(os.path.join(txt_path, image_name.replace('.jpg', '.txt')), 'w') as data:
                for bbox in data_list:
                    form = str(0) + ' ' + \
                           str(bbox[0]) + ' ' + str(bbox[1]) + ' ' + \
                           str(bbox[2]) + ' ' + str(bbox[3])
                    data.write(form + '\n')

        cv2.imshow('Detector', frame_copy)
    video.release()
    cv2.destroyAllWindows()


CONFIDENCE_THRESHOLD = 0.5
NMS_THRESHOLD = 0.6
COLORS = [(0, 255, 255), (255, 255, 0), (0, 255, 0), (255, 0, 0)]

# -------- Load Config / Weights --------
config_path = '../../Training_Process/coco_test/yolov4.cfg'
weights_path = '../../Training_Process/coco_test/yolov4.weights'
with open("../../Training_Process/coco_test/classes.txt", "r") as f:
    class_names = [cname.strip() for cname in f.readlines()]

# -------- Load Video --------
video_list_path = '../../Videos/0326_Testing_Video'

# -------- OpenCV Loading Yolov4 --------
net = cv2.dnn.readNet(weights_path, config_path)
net.setPreferableBackend(cv2.dnn.DNN_BACKEND_CUDA)
net.setPreferableTarget(cv2.dnn.DNN_TARGET_CUDA)
model = cv2.dnn_DetectionModel(net)
model.setInputParams(size=(416, 416), scale=1 / 255, swapRB=True)

print('[INFO] -------------------------------- ')
print('Detect Method: '.format('Yolov4'))
print('Config Path: {}\n'
      'Weights Path: {}'.format(config_path, weights_path))

for index, video_name in enumerate(os.listdir(video_list_path)):
    video_path = os.path.join(video_list_path, video_name)
    video_file_name = 'video-' + video_name.replace('.mp4', '')
    image_save_path = os.path.join('../../Dataset/', video_file_name)
    txt_file_path = os.path.join('../../Dataset/', video_file_name)

    print('Video Name: {}'.format(video_name))
    print('Video Path: {}'.format(video_path))
    print('Dataset Name: {}'.format(video_file_name))
    print('Frame Save Path: {}'.format(image_save_path))
    print('Text File Path: {}'.format(txt_file_path), '\n')

    Capture_From_Video(video_path, index, image_save_path, txt_file_path)
