from logging import getLogger, DEBUG

logger = getLogger(__name__)
logger.setLevel(DEBUG)

logger.debug('debug')
logger.info('info')
logger.warning('warning')
logger.error('error')
logger.critical('critical')

