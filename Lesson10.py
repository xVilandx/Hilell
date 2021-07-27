import os

current_dir = os.getcwd()
# print(current_dir)
#
list_dir = os.listdir()
# print(list_dir)

# tmp_path = os.path.join(current_dir)
# print(tmp_path)
files = []
for file_object in list_dir:
    if os.path.isfile(file_object):
        files.append(file_object)
print(files)

