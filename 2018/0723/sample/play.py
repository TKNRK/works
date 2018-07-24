import pyaudio
import wave
import sys
import time


input_filename = sys.argv[1]
buffer_size = 2**10
wav_file = wave.open (input_filename, 'rb')

p = pyaudio.PyAudio()

def callback(in_data, frame_count, time_info, status):
  data = wav_file.readframes(frame_count)
  return (data, pyaudio.paContinue)

stream = p.open(
             format = p.get_format_from_width(wav_file.getsampwidth()),
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

p.terminate()
