import logging

logging.basicConfig(filename='test.log',level='DEBUG',format='%(asctime)s: %(levelname)s: %(message)s')

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

logger.debug('Debug message')
logger.info('Info message')
logger.warning('Warning message')

logger.error('Error message')
logger.critical('Critical message')