import time
import os
from scipy import misc
import numpy as np
import concurrent.futures


def create_img(filename):
  # Create and save thumbnail image
  image = np.random.randint(0, 255, 100*100*3).reshape(100,100,3)
  misc.imsave(filename, image)
  return 1


# Loop through all jpeg files in the folder and make a thumbnail for each
if __name__ == '__main__':
  with concurrent.futures.ProcessPoolExecutor() as executor:
    startTime = time.time()
    lst = list(map(str, range(10000)))
    files = ["pics/"+num+".jpg" for num in lst]
    for file, _ in zip(files, executor.map(create_img, files)):
      print("created {0}".format(file))
    endTime = time.time()
    duration = endTime - startTime
    print("[benchmark] ", duration, "[s]")

