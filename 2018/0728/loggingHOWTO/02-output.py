import logging
import sys
import argparse


def _parse_arguments(argv):
    parser = argparse.ArgumentParser()
    parser.add_argument('-l', '--log', type=str, help='set loglevel (default level is WARNING)', default='WARNING', action='store')
    parser.add_argument('-f', '--filename', type=str, help='set filename (default name is example.log)', default='example.log', action='store')
    parser.add_argument('-o', '--overwrite', help='If true, overwrite the logfile', action='store_true')
    return parser.parse_args(argv)

ARGS = _parse_arguments(sys.argv[1:])
loglevel = ARGS.log
filename = ARGS.filename
filemode = 'w' if ARGS.overwrite else 'a'

numeric_level = getattr(logging, loglevel.upper(), None)
if not isinstance(numeric_level, int):
  raise ValueError('invalid log level: {}'.format(loglevel))

logging.basicConfig(filename=filename, filemode=filemode, level=numeric_level)

logging.debug('debug')
logging.info('info')
logging.warning('warning')
logging.error('error')
logging.critical('critical')
