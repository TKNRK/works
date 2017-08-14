import time
import os
from scipy import misc
import numpy as np


def create_img(filename):
  # Create and save thumbnail image
  image = np.random.randint(0, 255, 100*100*3).reshape(100,100,3)
  misc.imsave(filename, image)
  return 1


# Loop through all jpeg files in the folder and make a thumbnail for each
if __name__ == '__main__':
  startTime = time.time()
  lst = list(map(str, range(10000)))
  files = ["imgs/"+num+".jpg" for num in lst]
  for file in files:
    create_img(file)
    print("created {0}".format(file))
  endTime = time.time()
  duration = endTime - startTime
  print("[benchmark] ", duration, "[s]")