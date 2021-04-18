import os
import shutil

def zero_fill(file_list = [], ext = ".png"):
    maxlen = max([ len(x) for x in file_list ])
    print(">>> MAX:", maxlen)
    for item in file_list:
        new_name = item.zfill(maxlen)
        if item != new_name:
            print(f'{item} -> {new_name}')
            shutil.move(item, new_name)
        else:
            print(f'Ignoring {item} == {new_name}')

if __name__ == "__main__":
    print("Hello, world.")
    file_list = os.listdir(".")
    zero_fill(file_list = file_list)
