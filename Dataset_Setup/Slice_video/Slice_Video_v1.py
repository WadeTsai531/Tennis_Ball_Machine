import os
import cv2

video_path = ''
image_save_path = ''
pre_count = 10
count = 0
file_count = 0

video = cv2.VideoCapture(video_path)

while True:
    ret, frame = video.read()
    if not ret:
        break

    if count >= pre_count:
        cv2.imwrite(os.path.join(image_save_path, str(file_count) + '.jpg'), frame)
        print('Saving Image: {}'.format(os.path.join(image_save_path, str(file_count) + '.jpg')))
        count = 0
        file_count += 1
    else:
        count += 1
    cv2.imshow('image', frame)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break

point = len(str(len(os.listdir(image_save_path))))
new_count = 0
for file_name in os.listdir(image_save_path):
    new_name = str(new_count) + '.jpg'
    for pt in range(point - len(str(new_count))):
        new_name = '0' + new_name
    print('old Name: {} >>> New Name: {}'.format(file_name, new_name))
    os.renames(os.path.join(image_save_path, file_name),
               os.path.join(image_save_path, new_name))
    new_count += 1
