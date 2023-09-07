import os
import shutil

data_path = '../Training_Process/data_tennis'
dataset_path = '../../Dataset'
darknet_path = 'D:\\Wade\\Project\\Darknet_Project\\build\\darknet\\x64'

file_train = open(os.path.join(data_path, 'train.txt'), 'w')
file_test = open(os.path.join(data_path, 'test.txt'), 'w')

percentage_test = 10
counter = 1
index_test = round(100 / percentage_test)

for image_name in os.listdir(dataset_path):
	if image_name.split('.')[1] == 'txt' and image_name != 'classes.txt':
		if counter == index_test:
			counter = 1
			file_test.write(os.path.join(dataset_path.split('/')[1], image_name.replace('.txt', '.jpg')) + '\n')
		else:
			file_train.write(os.path.join(dataset_path.split('/')[1], image_name.replace('.txt', '.jpg')) + '\n')
			counter = counter + 1

