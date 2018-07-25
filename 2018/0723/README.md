# Audio Example

マルチスレッドな GUI の例．音声を録音するスレッドと wav を再生するスレッドを作ってみた．

## Requirement

- PyQt5
- pyaudio

pyaudio のインストールに必要

```
$ brew install portaudio
```

## reference

### QThread について

- [Qt Documentation: QThread Class](https://doc.qt.io/qt-5/qthread.html)
- [Python + PyQt5でGUIアプリを作ってみた](https://qiita.com/fukuit/items/2995950ed328140b9c18)
- [PyQt: Threading Basics Tutorial（PyQt4 なので注意）](https://nikolak.com/pyqt-threading-tutorial/)

### PyAudio について

- [http://hope-is-dream.hatenablog.com/entry/2016/11/21/Python%E3%81%A7%E9%9F%B3%E6%A5%BD%E5%86%8D%E7%94%9F_%7C_wave%2C_PyAudio](http://hope-is-dream.hatenablog.com/entry/2016/11/21/Python%E3%81%A7%E9%9F%B3%E6%A5%BD%E5%86%8D%E7%94%9F_%7C_wave%2C_PyAudio)
- [https://docs.python.jp/3/library/wave.html](https://docs.python.jp/3/library/wave.html)
- [https://people.csail.mit.edu/hubert/pyaudio/docs/](https://people.csail.mit.edu/hubert/pyaudio/docs/)