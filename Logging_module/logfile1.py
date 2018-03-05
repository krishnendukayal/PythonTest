import logging

logging.basicConfig(filename="krish.txt", level=logging.DEBUG)
logger = logging.getLogger(__name__)

# Info level msg
logger.info('This is a standard message')
# Debug level msg
logger.debug('This is what you may want to see... sometimes...')
# Warning level msg
logger.info('This is what you are usually not happy to see')