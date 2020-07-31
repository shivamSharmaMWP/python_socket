import socket
import logging
from logging.handlers import RotatingFileHandler
import os
from datetime import datetime


class LoggingHandler:
    _logger = None

    def initializeLogger(logger_name):

        # logging.basicConfig(level=os.environ.get("LOGLEVEL", "INFO"))

        log_file_path =  logger_name + "socket.log"

        l = logging.getLogger(logger_name)
        
        log_level = 'DEBUG'
        formatter = logging.Formatter("%(asctime)s: %(levelname)s: %(message)s")

        l.setLevel(log_level)

        rotating_file_handler = RotatingFileHandler(filename=log_file_path, mode='a', maxBytes=15728640, backupCount=1)
        rotating_file_handler.setFormatter(formatter)
    
        stream_handler = logging.StreamHandler()
        stream_handler.setFormatter(formatter)

        l.addHandler(rotating_file_handler)
        l.addHandler(stream_handler)    
        LoggingHandler._logger = l


    def getLogger(logger_name):
        if LoggingHandler._logger == None :
            LoggingHandler.initializeLogger(logger_name)
        return LoggingHandler._logger
    
