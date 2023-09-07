import os
import cv2

datasets_path = ''
Image_path = ''

folder_list = []

total = 0
for folder in folder_list:
    total += len(os.listdir(os.path.join(Image_path, folder)))
print('Total:', total)
point = len(str(total)) + 1
print('Point:', point)

count = 0
for folder_name in folder_list:
    for file_name in os.listdir(os.path.join(Image_path, folder_name)):
        if file_name != 'classes.txt':
            new_name = ''
            for pt in range(1, point + 1):
                if pt - len(str(count)) <= 0:
                    new_name = str(count)
                else:
                    new_name = '0' + new_name
            print('Old Name: {} >>> New Name: {}'.format(file_name, new_name + '.jpg'))
            image = cv2.imread(os.path.join(Image_path, folder_name, file_name))
            cv2.imwrite(os.path.join(datasets_path, new_name + '.jpg'), image)
            count += 1
