import os
import time

import cv2

video_path = '../../Videos'
dataset_path = '../../Dataset'
cap_temple = None
threshold = 0.98

for index, video_name in enumerate(os.listdir(video_path)[:1]):
	print('Video Name: {}'.format(video_name))

	cap = cv2.VideoCapture(os.path.join(video_path, video_name))

	print('Start')
	count = 0
	while cap.isOpened():
		ret, frame = cap.read()
		gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
		resize = cv2.resize(gray, (0, 0), 0, 0.3, 0.3)
		cv2.imshow('video', frame)
		cv2.imshow('image', resize)
		if cap_temple is None:
			cap_temple = resize
			cv2.imwrite(os.path.join(dataset_path, str(index) + '-' + str(count) + '.jpg'), frame)
			print('Save Image: {}'.format(os.path.join(dataset_path, str(index) + '-' + str(count) + '.jpg')))
			count += 1
		else:
			result = cv2.matchTemplate(resize, cap_temple, cv2.TM_CCOEFF_NORMED)
			result = round(result[0][0], 3)
			# cv2.imshow('temp', cap_temple)
			if result <= threshold:
				cap_temple = resize
				cv2.imwrite(os.path.join(dataset_path, str(index) + '-' + str(count) + '.jpg'), frame)
				print('Save Image: {}'.format(os.path.join(dataset_path, str(index) + '-' + str(count) + '.jpg')))
				count += 1

		if cv2.waitKey(1) & 0xff == ord('q'):
			break
	cap.release()
	cv2.destroyAllWindows()
