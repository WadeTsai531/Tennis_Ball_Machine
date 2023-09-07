import os
import time

import cv2

video_path = '../../Videos'
dataset_path = '../../Dataset'
cap_gray_temple = None
cap_resize_temple = None
threshold = 0.97

for index, video_name in enumerate(os.listdir(video_path)):
	print('Video Name: {}'.format(video_name))

	cap = cv2.VideoCapture(os.path.join(video_path, video_name))

	print('Start')
	count = 0
	while cap.isOpened():
		ret, frame = cap.read()
		resize = cv2.resize(frame, (0, 0), 0, 0.3, 0.3)
		gray = cv2.cvtColor(resize, cv2.COLOR_BGR2GRAY)

		cv2.imshow('Frame', frame)
		cv2.imshow('Resize', resize)
		cv2.imshow('Gray', gray)
		if cap_gray_temple is None:
			cap_gray_temple = gray
			cap_resize_temple = resize
			# cv2.imwrite(os.path.join(dataset_path, str(index) + '-' + str(count) + '.jpg'), frame)
			# print('Save Image: {}'.format(os.path.join(dataset_path, str(index) + '-' + str(count) + '.jpg')))
			# count += 1
		else:
			result_gray = cv2.matchTemplate(gray, cap_gray_temple, cv2.TM_CCOEFF_NORMED)
			result_gray = round(result_gray[0][0], 3)

			result_resize = cv2.matchTemplate(resize, cap_resize_temple, cv2.TM_CCOEFF_NORMED)
			result_resize = round(result_resize[0][0], 3)

			if result_gray <= threshold:
				cap_gray_temple = gray
			if result_resize <= threshold:
				cap_resize_temple = resize

			cv2.imshow('Temple Gray', cap_gray_temple)
			cv2.imshow('Temple Resize', cap_resize_temple)

			# print('Result Gray: {},  Result Resize: {}'.format())
			print(result_gray, result_resize)

		if cv2.waitKey(0) & 0xff == ord('q'):
			break
	cap.release()
	cv2.destroyAllWindows()
