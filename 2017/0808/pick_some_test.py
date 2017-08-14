import os
import random
import shutil

def pick_some(copy=False):
    root = "imgs/"
    target = "pictures/"
    img_paths = os.listdir(root)
    random.seed(0)
    random.shuffle(img_paths)
    if copy:
        operation = shutil.copy
    else:
        operation = shutil.move
    for file in img_paths[0:100]:
        operation(root + file, target)

if __name__ == "__main__":
    pick_some(copy=True)
