from PyQt5.QtCore import pyqtSignal, Qt, QMutexLocker, QMutex, QThread
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import datetime
import pyaudio
import wave
import time
import sys
from logging import getLogger, StreamHandler, DEBUG

logger = getLogger(__name__)
# handler = StreamHandler()
# handler.setLevel(DEBUG)
logger.setLevel(DEBUG)
# logger.addHandler(handler)
# logger.propagate = False


class RecordThread(QThread):

  def __init__(self, parent=None):
    super().__init__(parent)
    # プロパティの設定
    self.RECORD_SECONDS = 5 #録音する時間の長さ（秒）
    self.iDeviceIndex = 0 #録音デバイスのインデックス番号 
    self.FORMAT = pyaudio.paInt16 #音声のフォーマット
    self.CHANNELS = 1             #モノラル
    self.RATE = 44100             #サンプルレート
    self.CHUNK = 2**10            #データ点数

  def run(self):
    logger.info('Start AudioThread...')
    now = datetime.datetime.now()
    WAVE_OUTPUT_FILENAME = 'wav/{}.wav'.format(now.strftime('%Y-%m%d-%H%M%S'))

    audio = pyaudio.PyAudio()
    stream = audio.open(
            format=self.FORMAT,
            channels=self.CHANNELS,
            rate=self.RATE,
            input=True,
            input_device_index=self.iDeviceIndex,
            frames_per_buffer=self.CHUNK
          )

    logger.info('Start Recording...')
    frames = []
    # while(self.recording):
    for i in range(0, int(self.RATE / self.CHUNK * self.RECORD_SECONDS)):
        data = stream.read(self.CHUNK)
        frames.append(data)

    logger.info('Stop Recording.')
    stream.stop_stream()
    stream.close()
    audio.terminate()

    logger.info('Start Saving the Recording...')
    waveFile = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    waveFile.setnchannels(self.CHANNELS)
    waveFile.setsampwidth(audio.get_sample_size(self.FORMAT))
    waveFile.setframerate(self.RATE)
    waveFile.writeframes(b''.join(frames))
    waveFile.close()
    logger.info('Successfully Saved the Recording!')

  def recording_on(self):
    self.recording = True

  def recording_off(self):
    self.recording = False


class PlayThread(QThread):

  def __init__(self, parent=None):
    super().__init__(parent)

  def run(self):
    WAVE_INPUT_FILENAME = 'wav/se_maoudamashii_chime01.wav'
    wav_file = wave.open(WAVE_INPUT_FILENAME, 'rb')

    audio = pyaudio.PyAudio()

    def callback(in_data, frame_count, time_info, status):
      data = wav_file.readframes(frame_count)
      return (data, pyaudio.paContinue)

    stream = audio.open(
                 format = audio.get_format_from_width(wav_file.getsampwidth()),
                 channels = wav_file.getnchannels(),
                 rate = wav_file.getframerate(),
                 output = True,
                 stream_callback = callback
              )

    stream.start_stream()
    while stream.is_active():
      time.sleep(0.1)

    stream.stop_stream()
    stream.close()
    wav_file.close()

    audio.terminate()


class AudioWidget(QWidget):

  def __init__(self, style, parent=None):
    super().__init__(parent)

    # プロパティの設定
    self.RECORD_SECONDS = 5 #録音する時間の長さ（秒）
    self.iDeviceIndex = 0 #録音デバイスのインデックス番号
    self.FORMAT = pyaudio.paInt16 #音声のフォーマット
    self.CHANNELS = 1             #モノラル
    self.RATE = 44100             #サンプルレート
    self.CHUNK = 2**10            #データ点数

    # レイアウトの作成
    self.layout = QHBoxLayout()
    self.setLayout(self.layout)

    # アイコンの読み込み
    rec_icon = style.standardIcon(QStyle.StandardPixmap(QStyle.SP_DialogNoButton))
    play_icon = style.standardIcon(QStyle.StandardPixmap(QStyle.SP_MediaPlay))

    # ボタンの作成とアイコンの埋め込み
    btn_rec = QPushButton()
    btn_play = QPushButton()
    btn_rec.setIcon(rec_icon)
    btn_play.setIcon(play_icon)
    btn_rec.setToolTip('録音を開始します')
    btn_play.setToolTip('録音された音声を再生します')

    # 録音レイアウトの埋め込み
    self.layout.addWidget(btn_rec)
    self.layout.addWidget(btn_play)

    # 各ボタンの機能連携
    btn_rec.clicked.connect(self.start_rec)
    btn_play.clicked.connect(self.play_rec)

  def start_rec(self):
    self.record_thread = RecordThread()
    self.record_thread.start()

  def play_rec(self):
    self.play_thread = PlayThread()
    self.play_thread.start()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = AudioWidget(app.style())
    widget.resize(300, 100)
    widget.move(650, 50)
    widget.setWindowTitle('sample')
    widget.show()
    sys.exit(app.exec_())

