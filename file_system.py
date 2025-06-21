import os

def find_all_files(directory, depth=0):
    for item in os.listdir(directory):
        full_path = os.path.join(directory, item)
        if os.path.isdir(full_path):
            find_all_files(full_path, depth + 1)
        else:
            print(depth, f'Файл {item}')

directory = 'C:\\Users\\vital\\PycharmProjects\\Todo_list'
find_all_files(directory)





# directory = 'C:\\Users\\vital\\PycharmProjects\\Todo_list'
# print(os.listdir(directory))
# print(os.path.isdir(directory))
# path1 = 'C:\\Users\\vital'
# path2 = 'PycharmProjects\\Todo_list'
# print(os.path.join(path1, path2))