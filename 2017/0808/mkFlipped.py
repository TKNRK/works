import os
import numpy as np
from scipy import misc

files = os.listdir()
l = len(files)
for i in range(l):
  file = files[i]
  img = misc.imread(file)
  flipped = np.fliplr(img)
  misc.imsave("fl_"+file, flipped)
  if i % (l//20) == 0:
    progress = int((i / l) * 100)
    print("  [Processing] ... {0} %".format(progress))
