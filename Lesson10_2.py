# with open('lesson10.py', 'r') as py_file:
#     data = py_file.readlines()
#
# print(data)
#
# data.append('# Finish')
#
# with open('lesson10.3.py', 'w') as py_file:
#     py_file.writelines(data)
#
#
# with open('lesson10.py', 'r') as py_file:
#     data = py_file.readlines()
import os
import string


def create_dir(path):
    os.makedirs(path, exist_ok=True)


def create_file(file_name, symbol):
    with open(file_name, 'w') as txt_file:
        txt_file.write(string.ascii_lowercase.replace(symbol, symbol.upper()))


def create_files_in_dir(path):
    for letter in string.ascii_lowercase:
        file_name = f'{path}/{letter}.txt'
        create_file(file_name, letter)


def get_tanos_click(patch):
    files = os.listdir(patch)
    files = list(set(files))[:len(files) // 2]
    for file in files:
        os.remove(os.path.join(patch, file))


create_dir('alphabet')
create_files_in_dir('alphabet')
get_tanos_click('alphabet')