import sys
import time
from collections import deque
import logging
logging.basicConfig(filename='benchmark.log', level=logging.DEBUG)


def genEmpty():
  lst = []
  q = deque()
  s = set()
  dct = {}
  return {"list":lst, "deque":q, "set":s, "dictionary":dct}


def _append(N: int):
  dtypes = genEmpty()
  logging.info("{0} times iteration, TASK : APPEND".format(N))
  for dtype, d in dtypes.items():
    if dtype == "set":
      startTime = time.time()
      for i in range(N):
        d.add(i)
      endTime = time.time()
    elif dtype == "dictionary":
      startTime = time.time()
      for i in range(N):
        d.update({i:None})
      endTime = time.time()
    else:
      startTime = time.time()
      for i in range(N):
        d.append(i)
      endTime = time.time()
    logging.info("dtype: {0} [{1} sec]".format(dtype, (endTime - startTime) / N))


if __name__ == "__main__":
  _append(int(1e7))