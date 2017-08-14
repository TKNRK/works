# future 機能

参考ページ：

- [本家ドキュメント](https://docs.python.jp/3/library/concurrent.futures.html)
- [Qiita: Pythonでconcurrent.futuresを使った並列タスク実行](http://qiita.com/tag1216/items/db5adcf1ddcb67cfefc8)
- [Linked in: Speed up your Python data processing scripts with Process Pools](https://www.linkedin.com/pulse/speed-up-your-python-data-processing-scripts-process-pools-geitgey)

## future って？

非同期並列処理．将来的にこれやりますよって感じで並列を指定している．

Pure Python では Global Interpreter Lock があるため，真の並列は実装できない．
ので process pool によって並列計算を行う．

## 機能の使い方

### 1. パッケージをインポートする

```
import concurrent.futures
```

### 2. future を使いたいところに次の宣言をする

```
with concurrent.futures.ProcessPoolExecutor() as executor:
```

Executor は二種類ある．

### 3. future を使う　

```
def method(input):
  do something
  return done

inputs = iter(input)

with concurrent.futures.ProcessPoolExecutor() as executor:
  for input, done in zip(files, executor.map(method, inputs)):
    print(input, done)
```

### おまけ

- 使える CPU コア数を知りたい時

```
In [1]: import multiprocessing

In [2]: multiprocessing.cpu_count()
Out[2]: 8
```