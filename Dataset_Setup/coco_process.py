import os

path = 'D:\\Wade\\Project\\Darknet_Project\\test.txt'
new_path = 'D:\\Wade\\Project\\Darknet_Project\\test_2.txt'

file_test = open(new_path, 'w')


def test_fail_char(text):
    fail = ['.', '\\', '"', '?', '<', '>', '|', '\n', '·', ':']
    new_text = ''
    OK_flag = True
    for char in text:
        for fa in fail:
            if char == fa:
                OK_flag = False
                break
        if OK_flag:
            if char == ' ':
                new_text += '_'
            else:
                new_text += char
        OK_flag = True
    return new_text


with open(path, 'r') as f:
    for old_path in f.readlines():
        old_path = test_fail_char(old_path)
        new = 'coco_test/test2017/' + old_path.split('/')[3]
        print('{} ==> {}'.format(old_path, new))
        file_test.write(new + '\n')
