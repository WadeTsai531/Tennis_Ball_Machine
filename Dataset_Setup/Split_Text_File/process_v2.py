import os
import shutil

data_path = '/home/wade/Project/Tennis_Ball_Machine/Dataset/Training_Person_Datasets_1031'
text_file_path = '../../Training_Process/Training_Person_yolov4-tiny-L3_1031'

file_train = open(os.path.join(text_file_path, 'train.txt'), 'w')
file_test = open(os.path.join(text_file_path, 'test.txt'), 'w')

percentage_test = 10
counter = 1
index_test = round(100 / percentage_test)

print('Start')
for image_name in os.listdir(data_path):
    if image_name.split('.')[1] == 'txt' and image_name != 'classes.txt':
        if counter == index_test:
            counter = 1
            file_test.write(os.path.join(data_path, image_name.replace('.txt', '.jpg')) + '\n')
        else:
            file_train.write(os.path.join(data_path, image_name.replace('.txt', '.jpg')) + '\n')
            counter = counter + 1
print('over')
