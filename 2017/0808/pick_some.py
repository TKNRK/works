import os
import sys
import random
import shutil
import numpy as np

"""
root ディレクトリに存在するファイルをランダムに選び target ディレクトリに移すスクリプト
オプションによってディレクトリ上のファイル数を閲覧，moveの代わりにcopyを用いることができる．
また，ランダムに選ぶファイル数はデフォルトで 1000 である．
これはnumオプションに数字を打ち込むことで変更させることができる．

「使い方」
$ python pick_some.py root_dir target_dir [-l, -c] [num]

「オプション」
-l: ファイル数の閲覧
-c: move ではなく copy を使用
num: ランダムに選ぶファイル数を変更
"""


def _(root, target ,num, is_move=True):
  files = os.listdir(root)
  cnt = int(num)
  l = len(files)
  if cnt == 0:
    return -1

  random.seed(0)
  random.shuffle(files)

  if is_move: operation = shutil.move
  else:       operation = shutil.copy

  for i in range(cnt):
    file = files[i]
    operation(root + file, target)
    if (i % (cnt//10) == 0):
      progress = int((i / cnt) * 100)
      print("    [Processing] ... {0} %".format(progress))
  return 1

def pick_some(root:str, target:str, is_look=False, is_move=True, num_of_pick=1000):
  num = num_of_pick
  # -l オプションがついていたならファイルの数を表示する
  if is_look:
    root = argv[1]
    target = argv[2]
    files = len(os.listdir(root))
    copys = len(os.listdir(target))
    print("\n  There exists {0} files @ {1}".format(files, root))
    print("  There exists {0} files @ {1}\n".format(copys, target))
    return 1

  # ファイルの copy または move を実行する
  print("\n  From {0}, trying to get {1} files...".format(root, num))
  files_len1 = len(os.listdir(target))
  _(root, target, num, is_move)
  files_len2 = len(os.listdir(target))
  newfiles = files_len2 - files_len1
  print("  [Done] Added {0} files @ {1}\n".format(newfiles, target))


if __name__=='__main__':
  argv = sys.argv
  # 入力の長さは３以上５以下
  if len(argv) < 3 or len(argv) > 5:
    raise Exception("\n  invalid input length ...")
  # 入力が root, target のみならば copy する
  elif len(argv) == 3:
    pick_some(argv[1], argv[2])
  # 入力に -l オプションがあるならば is_look を True に
  elif "-l" in argv:
    argv.remove("-l")
    if len(argv) == 3:
      pick_some(argv[1], argv[2], is_look=True)
    else:
      raise Exception("\n  invalid syntacs ...")
  else:
    num_of_pick = "1000"
    is_move = True
    # 数字が入力に入っていたらそれが num_of_pick 引数になる
    for arg in argv:
      if str.isdigit(arg):
        num_of_pick = arg
    argv.remove(arg)
    # -c オプションならば move を copy に変更
    if "-c" in argv:
      argv.remove("-c")
      is_move = False
    # ここまでの処理で入力文字列の長さを３に削減できたら実行
    if len(argv) == 3:
      pick_some(argv[1], argv[2], is_move=is_move, num_of_pick=num_of_pick)

