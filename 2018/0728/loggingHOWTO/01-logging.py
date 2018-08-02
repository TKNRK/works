import logging
import sys
import argparse

def _parse_arguments(argv):
    parser = argparse.ArgumentParser()
    parser.add_argument('-l', '--log', type=str, help='set loglevel (default level is WARNING)', default='WARNING', action='store')
    return parser.parse_args(argv)

ARGS = _parse_arguments(sys.argv[1:])
loglevel = ARGS.log

numeric_level = getattr(logging, loglevel.upper(), None)
if not isinstance(numeric_level, int):
  raise ValueError('invalid log level: {}'.format(loglevel))

logging.basicConfig(level=numeric_level)

logging.debug('debug')
logging.info('info')
logging.warning('warning')
logging.error('error')
logging.critical('critical')
