# Python を用いた文字列置換

別のあるファイルの中にある特定の文字列を置換するスクリプトを作った．

参考：
[ブログ](http://python.slightlysimple.net/entry/2015/05/06/131644)

## 使用方法

```
from file_replacement import subs_file

file        = "置換対象のファイル名"
new_file    = "置換後のファイル名"
txt_old     = "置換対象の文字列"
txt_new     = "置換後の文字列"
replacement = {txt_old: txt_new}

subsfile(file, new_file, replacement)
```

ファイル中の文字列がまるっと置き換わる．サンプル参照．