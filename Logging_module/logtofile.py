import logging
from datetime import datetime as dt


print(dt.now())
logging.basicConfig(filename="logfile.txt", level=logging.DEBUG)
logging.debug("This is debug message during program exection")
logging.error("This is error message")
logging.warning("This is warning message")
logging.critical("This is critical message")
logging.info("This is info message")
