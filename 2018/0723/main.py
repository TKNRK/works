import os
import sys
from PyQt5.QtCore import pyqtSignal, Qt
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.Qt import QFont
from logging import getLogger, StreamHandler, DEBUG

from audio_widget import AudioWidget

logger = getLogger(__name__)
# handler = StreamHandler()
# handler.setLevel(DEBUG)
logger.setLevel(DEBUG)
# logger.addHandler(handler)
# logger.propagate = False


"""
TODO:

- AudioThread の録音を任意のタイミングで終了する機能を追加する
- AudioThread で録音開始，録音終了の状態に応じてアイコンを変える
- 作成したThread の解放（メモリリークが起きる？）
- logger の handler とかを調べる
"""


class AudioSample(QWidget):
  def __init__(self, parent=None):
    super().__init__()

    ###############################################
    ### 履歴ボタンの記述
    ###############################################
    style = self.app.style()
    audio_widget = AudioWidget(style)

    ###############################################
    ### レイアウトの埋め込み
    ###############################################
    mainLayout = QHBoxLayout()
    mainLayout.setAlignment(Qt.AlignTop)
    mainLayout.addWidget(audio_widget)
    self.setLayout(mainLayout)
    self.setWindowTitle("Audio sample")

  @classmethod
  def start(cls, fullscreen=False):
    cls.app = QApplication(sys.argv)
    widget = cls()
    widget.resize(300, 100)
    widget.move(650, 50)
    widget.show()
    if fullscreen:
        widget.windowHandle().setVisibility(QWindow.FullScreen)
    sys.exit(cls.app.exec_())

  def keyPressEvent(self, ev):
    k = ev.key()
    if k == Qt.Key_Escape or k == Qt.Key_Q:
        self.close()
        try:
            sys.exit(self.app.exec_())
        except:
            print("exiting")

  # def closeEvent(self, event):
  #     close = QMessageBox()
  #     close.setText('Quit?')
  #     close.setStandardButtons(QMessageBox.Yes | QMessageBox.Cancel)
  #     close = close.exec()
  #
  #     if close == QMessageBox.Yes:
  #         event.accept()
  #     else:
  #         event.ignore()


if __name__ == '__main__':
  AudioSample.start(fullscreen=False)

