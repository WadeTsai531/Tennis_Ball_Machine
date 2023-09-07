import xml.etree.ElementTree as ET
import os


class Main:
    def __init__(self):
        self.xml_Dataset_path = '../Dataset/COCO_xml/'
        self.yolo_Dataset_path = '../Dataset/COCO_Image/'

        for file in os.listdir(self.xml_Dataset_path):
            if file.split('.')[1] == 'xml':
                Data = self.Read_xml(os.path.join(self.xml_Dataset_path, file))
                self.write_txt(file, Data)

    def Read_xml(self, file_name):
        tree = ET.parse(file_name)
        root = tree.getroot()

        image_width = int(root.find('size').find('width').text)
        image_height = int(root.find('size').find('height').text)

        print(image_width, image_height)
        data = []
        for index, country in enumerate(root.findall('object')):
            name = country.find('name').text
            difficult = int(country.find('difficult').text)
            if difficult == 0:
                xmin = int(country.find('bndbox').find('xmin').text)
                ymin = int(country.find('bndbox').find('ymin').text)
                xmax = int(country.find('bndbox').find('xmax').text)
                ymax = int(country.find('bndbox').find('ymax').text)

                yolo_x_center, yolo_y_center, yolo_w, yolo_h = self.xml_to_yolo_bbox([xmin, ymin,
                                                                                      xmax, ymax],
                                                                                     image_width, image_height)
                print(index, name, xmin, ymin, xmax, ymax, '>>>',
                      yolo_x_center, yolo_y_center, yolo_w, yolo_h)
                data.append([yolo_x_center, yolo_y_center, yolo_w, yolo_h])
        return data

    def write_txt(self, file_name, data):
        with open(os.path.join(self.yolo_Dataset_path, file_name.replace('xml', 'txt')), 'w') as f:
            for bbox in data:
                f.write('0' + ' ' + str(bbox[0]) + ' ' + str(bbox[1]) + ' ' + str(bbox[2]) + ' ' + str(bbox[3]) + '\n')

    def xml_to_yolo_bbox(self, bbox, w, h):
        x_center = ((bbox[2] + bbox[0]) / 2) / w
        y_center = ((bbox[3] + bbox[1]) / 2) / h
        width = (bbox[2] - bbox[0]) / w
        height = (bbox[3] - bbox[1]) / h
        return [x_center, y_center, width, height]


Main()
