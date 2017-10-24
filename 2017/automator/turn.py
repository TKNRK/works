# 順番生成のためのライブラリ
import random
import datetime
# 文字列置換のためのライブラリ
import re
import codecs
import glob
# io のためのライブラリ
import os
import sys

###########################################
## 順番の生成
###########################################
def gen_turn(members, seed=None):
  # seed がなければ今日の日付を seed にする
  if not (isinstance(seed, int)):
    t = datetime.date.today()
    y, m, d = t.year, t.month, t.day
    date = str(y) + str(m) + str(d)
    seed = int(data)

  # members が iterable かチェック
  try:
    lst_members = list(members)
  except:
    raise Exception("[ERROR] invalid members type at gen_turn@turn.py...")

  random.seed(seed)
  shuffled = random.sample(lst_members, len(lst_members))
  turns = ""
  # markdown の表を置換するための文字列
  for member in shuffled:
    turns += "|" + str(member) + "|\n"

  return turns

###########################################
## readmeの生成
###########################################
def subs_file(file, file_new, words):
  '''
  file     : str           ...置換するファイル名
  file_new : str           ...置換後のファイル名
  words    : dict{str:str} ...文字の置換ルール
  '''

  if not os.path.exists(file):
    raise Exception("[ERROR] such template doesnt exist...")

  read_file = codecs.open(file, 'r', 'cp932')
  write_file = codecs.open(file_new, 'w', 'cp932')

  lines = read_file.readlines() # 読み込み
  lines2 = []

  # 全ての置換ルールについて文字列置換を適用する
  for key in words:
    txt_old = key         # ファイル内の置換前文字列
    txt_new = words[key]  # ファイル内の置換後文字列

    for line in lines:
        line = line.replace(txt_old,txt_new) # テキスト置換
        lines2.append(line) # 別リストにする

    lines = lines2
    lines2 = []

  write_file.write(''.join(lines)) # 書き込み
  read_file.close()
  write_file.close()


if __name__ == '__main__':

  argv = sys.argv
  print(argv)
  len_argv = len(argv)

  if not len_argv == 2:
    raise Exception("[ERROR] invalid argument")

  members = [
    "takeda", "takano", "ito",
    "sakamoto", "tazoe"
  ]

  MEMBERS = gen_turn(members)

  template = "/Users/takano/Dropbox/wlab/17-allhands/template.md"
  readme = argv[1]
  subs_file(template, readme, {"MEMBERS":MEMBERS})
