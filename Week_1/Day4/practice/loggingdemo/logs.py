import logging
logging.basicConfig(filename="mylog.log", level=logging.DEBUG)
format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'

#this logs it into the console, but you can log it into a file
logging.info("This is an info message")
logging.debug("This is a debug message")
logging.error("This is an error message")
logging.critical("This is critical message")
logging.warning("This is warning message")


