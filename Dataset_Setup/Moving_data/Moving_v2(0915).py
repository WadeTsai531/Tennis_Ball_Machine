import os
import shutil
import glob


class Main:
    old_xml_path = '../../Dataset/COCO_xml'
    new_xml_path = '../Dataset/Person_Detection_0916-Datasets'
    image_path = 'E:\\Person_Detection_0914-yolov4_tiny'
    pos_image_path = '../Dataset/Person_Detection_0914-yolov4_tiny'
    final_path = new_xml_path
    # 'F:\\Dataset\\Person_Detection_0915-yolov4_tiny'

    def __init__(self):
        # self.Combine()
        # self.Moving()
        # self.Delete()
        self.Rename_Pos()

    def Combine(self):
        for folder_name in os.listdir(self.old_xml_path):
            print('Now Folder:', folder_name)
            for file_name in os.listdir(os.path.join(self.old_xml_path, folder_name)):
                if not os.path.exists(os.path.join(self.new_xml_path, file_name)):
                    print('File Name: {} Moving to {}\\{}'.format(file_name, self.new_xml_path, file_name))
                    os.renames(os.path.join(self.old_xml_path, folder_name, file_name),
                               os.path.join(self.new_xml_path, file_name))

    def Moving(self):
        for file_name in os.listdir(self.image_path):
            if file_name.split('.')[1] == 'jpg':
                new_path = os.path.join(self.final_path, file_name)
                print('File Name: {} >>> {}'.format(file_name, new_path))
                shutil.copyfile(os.path.join(self.image_path, file_name), new_path)

    def Rename_Coco(self):
        name_index = len(str(len(os.listdir(self.old_xml_path))))
        for index, xml_file in enumerate(os.listdir(self.old_xml_path)):
            new_name = str(index+1)
            for _ in range(name_index):
                if len(new_name) < name_index:
                    new_name = '0' + new_name
            new_name += '.xml'
            print('Xml File: {} >>> {}'.format(xml_file, new_name))
            shutil.copyfile(os.path.join(self.old_xml_path, xml_file),
                            os.path.join(self.final_path, new_name))

    def Rename_Pos(self):
        count = 64532
        for index, file_name in enumerate(os.listdir(self.pos_image_path)):
            if file_name.split('.')[1] == 'jpg':
                print('Image Name: {} >>> {}'.format(file_name, str(count) + '.jpg'), end=', ')
                print('label Name: {} >>> {}'.format(file_name.replace('jpg', 'txt'), str(count) + '.txt'))

                shutil.copyfile(os.path.join(self.pos_image_path, file_name),
                                os.path.join(self.final_path, str(count) + '.jpg'))
                shutil.copyfile(os.path.join(self.pos_image_path, file_name.replace('jpg', 'txt')),
                                os.path.join(self.final_path, str(count) + '.txt'))
                count += 1

    def Delete(self):
        for file_name in os.listdir(self.final_path):
            if file_name.split('.')[1] == 'xml':
                print('Delete File:', file_name)
                os.remove(os.path.join(self.final_path, file_name))


Main()
