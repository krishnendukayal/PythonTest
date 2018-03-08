import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

formatter=logging.Formatter('%(levelname)s:%(name)s:%(message)s')

file_handeler=logging.FileHandler("krishnendu_kayal.txt")
file_handeler.setFormatter()


