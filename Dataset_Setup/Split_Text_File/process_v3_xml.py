import math
import os
import random
import re
import shutil


class Main:
	def __init__(self):
		self.image_dir = '/Dataset'
		self.output_dir =  'D:\\Wade\\Project\\Tensorflow_API\\training_tf_0528_v1\\images'

		self.image_dir = self.image_dir.replace('\\', '/')
		self.output_dir = self.output_dir.replace('\\', '/')

		self.iterate_dir()

	def iterate_dir(self):
		train_dir = os.path.join(self.output_dir, 'train')
		test_dir = os.path.join(self.output_dir, 'test')

		if not os.path.exists(train_dir):
			os.makedirs(train_dir)
		if not os.path.exists(test_dir):
			os.makedirs(test_dir)

		images = []
		num_image = 0
		for index_1, file in enumerate(os.listdir(self.image_dir)):
			if os.path.isdir(os.path.join(self.image_dir, file)):
				for index_2, file_2 in enumerate(os.listdir(os.path.join(self.image_dir, file))):
					if len(file_2.split('.txt')) > 1 and file_2 != 'classes.txt' \
						and os.path.isfile(os.path.join(self.image_dir, file, file_2.replace('.txt', '.jpg'))):
						num_image += 1
						images.append(os.path.join(self.image_dir, file, file_2.replace('.txt', '.jpg')))
			else:
				if len(file.split('.txt')) > 1 and file != 'classes.txt' \
					and os.path.isfile(os.path.join(self.image_dir, file.replace('.txt', '.jpg'))):
					num_image += 1
					images.append(os.path.join(self.image_dir, file.replace('.txt', '.jpg')))
		num_test_image = math.ceil(0.2 * num_image)
		print('Image Quantity: {} -- Image test: {}'.format(num_image, num_test_image))

		for i in range(num_test_image):
			index = random.randint(0, num_image-1)
			file_name = images[index]
			shutil.copyfile(file_name,
							os.path.join(test_dir, file_name.split('\\')[-1]))





Main()

# file_train = open(os.path.join(text_file_path, 'train.txt'), 'w')
# file_test = open(os.path.join(text_file_path, 'test.txt'), 'w')
#
# percentage_test = 10
# counter = 1
# index_test = round(100 / percentage_test)
#
# for photo_name in os.listdir(data_path):
# 	if photo_name != 'Video_1' and photo_name != 'classes.txt':
# 		for image_name in os.listdir(os.path.join(data_path, photo_name)):
# 			if image_name.split('.')[1] == 'txt' and image_name != 'classes.txt':
# 				if counter == index_test:
# 					counter = 1
# 					file_test.write(os.path.join(data_path, photo_name,
# 												 image_name.replace('.txt', '.jpg')) + '\n')
# 				else:
# 					file_train.write(os.path.join(data_path, photo_name,
# 												  image_name.replace('.txt', '.jpg')) + '\n')
# 					counter = counter + 1

