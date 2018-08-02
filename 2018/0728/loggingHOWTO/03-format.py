import logging

logging.basicConfig(
      format='[%(levelname)s]%(name)s: %(asctime)s\n    %(message)s',
      datefmt='%Y/%m/%d %H:%M:%S',
      level=logging.DEBUG)

logging.debug('This message should appear on the console')
logging.info('So should this')
logging.warning('And this, too')