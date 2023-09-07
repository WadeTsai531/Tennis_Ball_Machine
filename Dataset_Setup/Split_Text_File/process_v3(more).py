import os

data_path = ['/home/wade/Project/Tennis_Ball_Machine/Dataset/COCO_Datasets']
text_file_path = '../../Training_Process/Person_Training-yolov4_tiny_288-1214-coco'
file_train = open(os.path.join(text_file_path, 'train.txt'), 'w')
file_test = open(os.path.join(text_file_path, 'test.txt'), 'w')
percentage_test = 20
counter = 1
index_test = round(100 / percentage_test)

print('Start')
for folder in data_path:
    for image_name in os.listdir(folder):
        print(image_name)
        if image_name.split('.')[1] == 'txt' and image_name != 'classes.txt':
            if counter == index_test:
                counter = 1
                file_test.write(os.path.join(folder, image_name.replace('.txt', '.jpg')) + '\n')
            else:
                file_train.write(os.path.join(folder, image_name.replace('.txt', '.jpg')) + '\n')
                counter = counter + 1
print('OK')
