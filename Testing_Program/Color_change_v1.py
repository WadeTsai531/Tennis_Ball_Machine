import cv2
import os
import numpy as np


def yolo_to_xml_bbox(bbox, w, h):
    w_half_len = (bbox[2] * w) / 2
    h_half_len = (bbox[3] * h) / 2
    xmin = int((bbox[0] * w) - w_half_len)
    ymin = int((bbox[1] * h) - h_half_len)
    xmax = int((bbox[0] * w) + w_half_len)
    ymax = int((bbox[1] * h) + h_half_len)
    return [xmin, ymin, xmax, ymax]


def Read_Text_file(file_name):
    with open(file_name, 'r') as f:
        read_data = f.readlines()
    return read_data


class Main:
    def __init__(self):
        Dataset_path = '../Dataset/Person_Training_0914/'
        Converted_path = '../Dataset/Person_Training_0914(converted)/'

        for index, file_name in enumerate(os.listdir(Dataset_path)):
            if file_name.split('.')[1] == 'jpg':
                print('Processing Image:', file_name)
                image = cv2.imread(os.path.join(Dataset_path, file_name))
                image = cv2.resize(image, None, fx=0.4, fy=0.4)
                h, w = image.shape[:2]
                print('Image Shape W: {}, H: {}'.format(w, h))
                bbox = self.ROI(w, h, os.path.join(Dataset_path, file_name).replace('jpg', 'txt'))

                image_draw = image.copy()
                for index_box, box in enumerate(bbox):
                    cv2.rectangle(image_draw, (box[0], box[1]), (box[2], box[3]), (255, 0, 255), 3)
                    image_roi = image[box[1]:box[3], box[0]:box[2]]
                    new_image_roi = self.color_change(image_roi)
                    image_draw[box[1]:box[3], box[0]:box[2]] = new_image_roi
                    image[box[1]:box[3], box[0]:box[2]] = new_image_roi

                cv2.imwrite(os.path.join(Converted_path, file_name), image)
                cv2.imshow('image', image)
                cv2.waitKey(500)
                # cv2.destroyAllWindows()

    def ROI(self, w, h, text_name):
        text_data = Read_Text_file(text_name)
        bbox = []
        for index, obj in enumerate(text_data):
            print('Target {}: '.format(index+1), end='')
            sbox = []
            for box in obj[:-1].split(' ')[1:]:
                sbox.append(float(box))
            print(yolo_to_xml_bbox(sbox, w, h))
            bbox.append(yolo_to_xml_bbox(sbox, w, h))
        return bbox

    def color_change(self, image_roi, color=(0, 0, 255)):
        lower_blue = np.array([110, 160, 100])
        upper_blue = np.array([127, 255, 255])
        h, w = image_roi.shape[:2]
        image_change = cv2.cvtColor(image_roi, cv2.COLOR_BGR2HSV)
        blue_mask = cv2.inRange(image_change, lower_blue, upper_blue)
        red_image = np.zeros((h, w, 3), np.uint8)
        red_image[0:h, 0:w] = color
        red_roi = cv2.bitwise_and(red_image, red_image, mask=blue_mask)
        image_roi_inv = cv2.bitwise_and(image_roi, image_roi, mask=~blue_mask)
        result = cv2.add(red_roi, image_roi_inv)
        return result


Main()
