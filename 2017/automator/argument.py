import sys
import codecs

if __name__ == '__main__':
  argv = sys.argv
  print(argv)
  len_argv = len(argv)

  if (len_argv == 1):
    print("hello")
  elif (len_argv == 2):
    try:
      i = int(argv[1])
      print(i * 2)
    except:
      print(argv[1])
  else:
    print("too long")

  write_file = codecs.open("/Users/takano/Desktop/argument.txt", 'w', 'cp932')
  write_file.write('\n'.join(argv))