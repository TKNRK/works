import sys
import argparse

def _parse_arguments(argv):

  parser = argparse.ArgumentParser()
  parser.add_argument('--hoge', type=str, default="2",
                      help="number to pow")
  parser.add_argument('--huga', type=str, default="2",
                      help="huga huga")
  return parser.parse_args(argv)

def _(args):
  ans = int(args.hoge) ** int(args.huga)
  print(ans)
  return ans


if __name__ == "__main__":
  _(_parse_arguments(sys.argv[1:]))
