import numpy as np
import cv2
import os
import time
import concurrent.futures


def distort(filename):
  file = filename.split("/")[-1]
  header = filename.strip(file)
  src = cv2.imread(filename, 1)

  #１．コントラストの調整
  min_table = 50
  max_table = 205
  diff_table = max_table - min_table
  LUT_HC = np.arange(256, dtype = 'uint8' )
  LUT_LC = np.arange(256, dtype = 'uint8' )
  for i in range(0, min_table):
      LUT_HC[i] = 0
  for i in range(min_table, max_table):
      LUT_HC[i] = 255 * (i - min_table) / diff_table
  for i in range(max_table, 255):
      LUT_HC[i] = 255
  for i in range(256):
      LUT_LC[i] = min_table + i * (diff_table) / 255
  high_cont_img = cv2.LUT(src, LUT_HC)
  low_cont_img = cv2.LUT(src, LUT_LC)
  cv2.imwrite(header+"hc_"+file, high_cont_img)
  cv2.imwrite(header+"lc_"+file, low_cont_img)

  # ２．平坦か
  average_square = (10,10)
  blur_img = cv2.blur(src, average_square)
  cv2.imwrite(header+"bl_"+file, blur_img)

  # ３．ガウスノイズ
  row,col,ch= src.shape
  mean = 0
  sigma = 15
  gauss = np.random.normal(mean,sigma,(row,col,ch))
  gauss = gauss.reshape(row,col,ch)
  gauss_img = src + gauss
  cv2.imwrite(header+"ga_"+file, gauss_img)

  # ４．ソルトペッパーノイズ
  row,col,ch = src.shape
  s_vs_p = 0.5
  amount = 0.004
  sp_img = src.copy()
  num_salt = np.ceil(amount * src.size * s_vs_p)
  coords = [np.random.randint(0, i-1 , int(num_salt)) for i in src.shape]
  sp_img[coords[:-1]] = (255,255,255)
  num_pepper = np.ceil(amount* src.size * (1. - s_vs_p))
  coords = [np.random.randint(0, i-1 , int(num_pepper)) for i in src.shape]
  sp_img[coords[:-1]] = (0,0,0)
  cv2.imwrite(header+"sp_"+file, sp_img)


if __name__ == '__main__':
  print("\n  concurrent.future start")
  with concurrent.futures.ProcessPoolExecutor() as executor:
    startTime = time.time()
    # place where image files exist
    root = "imgs/"
    lst = os.listdir(root)
    l = len(lst)
    files = [root + file for file in lst]

    for _, _ in zip(files, executor.map(distort, files)):
      pass

    endTime = time.time()
    duration = endTime - startTime
    print("[benchmark] ", duration, "[s]")



