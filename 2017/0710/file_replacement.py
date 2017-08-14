# coding: UTF-8
import re
import codecs, os
import glob

def subs_file(file, file_new, words):
  '''
  file     : str           ...置換するファイル名
  file_new : str           ...置換後のファイル名
  words    : dict{str:str} ...文字の置換ルール
  '''

  # TODO: ファイルの存在検知，置換後のファイルでディレクトリが存在するか？

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
  subs_file("template.py", "new.py", {"hello":"10", "num_of_nodes":"100"})
  subs_file("template.cs", "new.cs", {"NUM_OF_NODES":"111", "DIMENTION": "66"})
  subs_file("template.shaders", "new.shaderes", {"number":"100"})