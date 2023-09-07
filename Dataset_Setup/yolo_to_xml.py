import xml.etree.ElementTree as ET
import glob
import os
import numpy as np
import json
import cv2


class Convert_Pascal:
    def __init__(self):
        self.yolo_path = '../Dataset/Convert_Data/'
        self.pascal_path = '../Dataset/Convert_Data/'

        classes_path = '../Dataset/classes.txt'
        with open(classes_path) as f:
            self.classes = f.readlines()

        self.convert()

    def convert(self):
        total_index = 0
        print('Start Convert')
        for index_1, file in enumerate(os.listdir(self.yolo_path)):
            if os.path.isdir(os.path.join(self.yolo_path, file)):
                for index_2, file_2 in enumerate(os.listdir(os.path.join(self.yolo_path, file))):
                    if len(file_2.split('.txt')) > 1 and file_2 != 'classes.txt' \
                            and os.path.isfile(os.path.join(self.yolo_path, file, file_2.replace('.txt', '.jpg'))):
                        total_index += 1

                        folder = file
                        file_name = file_2.replace('.txt', '.jpg')
                        path = os.path.join(os.getcwd(), self.yolo_path.split('/')[1], file, file_name)
                        image_shape = cv2.imread(os.path.join(self.yolo_path, file, file_name)).shape

                        print('---------------------------------')
                        print('[Data Path]: {}'.format(path))
                        print('[File Name]: {} -- [Image Name]: {}'.format(folder, file_name))
                        All_bboxes = self.read_txt_file(os.path.join(self.yolo_path, file, file_2), image_shape)
                        self.Write_XML_File(os.path.join(self.yolo_path, file),
                                            folder, file_name, path, image_shape, All_bboxes)
                        print('=================================\n')

            else:
                if len(file.split('.txt')) > 1 and file != 'classes.txt' \
                        and os.path.isfile(os.path.join(self.yolo_path, file.replace('.txt', '.jpg'))):
                    total_index += 1

                    folder = self.yolo_path.split('/')[1]
                    file_name = file.replace('.txt', '.jpg')
                    path = os.path.join(os.getcwd(), self.yolo_path.split('/')[1], file_name)
        print(total_index)

    def xml_to_yolo_bbox(self, bbox, w, h):
        x_center = ((bbox[2] + bbox[0]) / 2) / w
        y_center = ((bbox[3] + bbox[1]) / 2) / h
        width = (bbox[2] - bbox[0]) / w
        height = (bbox[3] - bbox[1]) / h
        return [x_center, y_center, width, height]

    def yolo_to_xml_bbox(self, bbox, w, h):
        w_half_len = (bbox[2] * w) / 2
        h_half_len = (bbox[3] * h) / 2
        xmin = int((bbox[0] * w) - w_half_len)
        ymin = int((bbox[1] * h) - h_half_len)
        xmax = int((bbox[0] * w) + w_half_len)
        ymax = int((bbox[1] * h) + h_half_len)
        return [xmin, ymin, xmax, ymax]

    def read_txt_file(self, file_name, image_shape):
        with open(file_name) as f:
            text = f.readlines()

        h, w = image_shape[:2]

        All_bboxes = []
        for data in text:
            data = data.replace('\n', '')
            detail_list = data.split(' ')
            coordinate = self.yolo_to_xml_bbox([float(detail_list[1]),
                                                float(detail_list[2]),
                                                float(detail_list[3]),
                                                float(detail_list[4])],
                                               w, h)
            label_name = self.classes[int(detail_list[0])]
            All_bboxes.append({"xmin": coordinate[0],
                               "xmax": coordinate[2],
                               "ymin": coordinate[1],
                               "ymax": coordinate[3],
                               "Label": label_name})
            print('Annotation: {} -- Label: {}'.format(coordinate, label_name))
        return All_bboxes

    def Write_XML_File(self, Base_Path, folder, filename, path, image_shape, All_bboxes):
        # -------- Write XML File --------
        annotation = ET.Element('annotation')
        ET.SubElement(annotation, 'folder').text = str(folder)
        ET.SubElement(annotation, 'filename').text = str(filename)
        ET.SubElement(annotation, 'path').text = str(path)
        source = ET.SubElement(annotation, 'source')
        ET.SubElement(source, 'database').text = 'Unknown'
        size = ET.SubElement(annotation, 'size')
        ET.SubElement(size, 'width').text = str(image_shape[1])
        ET.SubElement(size, 'height').text = str(image_shape[0])
        ET.SubElement(size, 'depth').text = str(image_shape[2])
        ET.SubElement(annotation, 'segmented').text = '0'

        for item in All_bboxes:
            label = item['Label']
            xmax = item['xmax']
            xmin = item['xmin']
            ymax = item['ymax']
            ymin = item['ymin']

            xml_object = ET.SubElement(annotation, 'object')
            ET.SubElement(xml_object, 'name').text = label
            ET.SubElement(xml_object, 'pose').text = 'Unspecified'
            ET.SubElement(xml_object, 'truncated').text = '0'
            ET.SubElement(xml_object, 'difficult').text = '0'
            bndbox = ET.SubElement(xml_object, 'bndbox')
            ET.SubElement(bndbox, 'xmin').text = str(xmin)
            ET.SubElement(bndbox, 'ymin').text = str(ymin)
            ET.SubElement(bndbox, 'xmax').text = str(xmax)
            ET.SubElement(bndbox, 'ymax').text = str(ymax)

        tree = ET.ElementTree(annotation)
        xml_file_name = os.path.join(self.pascal_path, filename.replace('.jpg', '.xml'))
        tree.write(xml_file_name)


Convert_Pascal()
