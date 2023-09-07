import os

base_path = '../Dataset/Person_Detection_0916-Datasets'
name_index = len(str(len(os.listdir(base_path))))-1
for i in range(1, len(os.listdir(base_path))+1):
    new_name = str(i)
    for _ in range(name_index):
        if len(new_name) < name_index:
            new_name = '0' + new_name
    new_name += '.jpg'
    if os.path.isfile(os.path.join(base_path, new_name)):
        print(new_name, '>>> OK')
    else:
        print(new_name, '>>> ERROR')
        break
