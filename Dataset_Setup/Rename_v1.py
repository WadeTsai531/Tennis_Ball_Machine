import os

data_path = 'H:\\Learning\\Dataset'

total = (len(os.listdir(data_path)) - 1) // 2
print('Total: {}'.format(total))

point = len(str(total)) + 1
print(point)

for file_name in os.listdir(data_path):
    if file_name != 'classes.txt':
        index = len(file_name.split('.')[0])
        new_name = '.' + file_name.split('.')[1]
        for pt in range(1, point+1):
            if pt - index <= 0:
                new_name = file_name.split('.')[0][-pt] + new_name
            else:
                new_name = '0' + new_name
        print('Old Name: {} >>> New Name: {}'.format(file_name, new_name))
        os.renames(os.path.join(data_path, file_name),
                   os.path.join(data_path, new_name))
