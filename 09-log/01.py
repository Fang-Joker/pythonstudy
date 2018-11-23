import logging

# 自定义格式, %(相应内容)s
LOG_GORMAT = "%(asctime)s====%(levelname)s++++%(message)s"
# 进行配置
logging.basicConfig(filename="tx.log",level=logging.DEBUG,format=LOG_GORMAT)

# 如果不进行配置，默认只输出warning及其以上的错误
logging.debug("This is a debug log")
logging.info("This is a debug log")
logging.warning("This is a debug log")
logging.error("This is a debug log")
logging.critical("This is a debug log")

logging.log(logging.DEBUG,"This is a log")
logging.log(logging.INFO,"This is a log")
logging.log(logging.WARNING,"This is a log")
logging.log(logging.ERROR,"This is a log")
logging.log(logging.CRITICAL,"This is a log")
