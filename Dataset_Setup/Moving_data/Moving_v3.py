import os
import shutil

datasets_path = '/media/wade/DA08618C08616889/train2017/'
dir_path = '/home/wade/Project/Glsan/detectron2/datasets/coco/train2017/'

for index, file_name in enumerate(os.listdir(datasets_path)):
    print('Index: {} -- {} >>> {}'.format(index, os.path.join(datasets_path, file_name),
                                          os.path.join(dir_path, file_name)))
    shutil.copyfile(os.path.join(datasets_path, file_name), os.path.join(dir_path, file_name))
