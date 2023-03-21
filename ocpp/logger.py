from logging.config import dictConfig
import logging
import sys, os
from os.path import exists

def checkLogFile():
    if exists('./log'):
        pass
    else:
        os.makedirs('./log')

class LOGGER():

    def __init__(self):
        checkLogFile()

        dictConfig({
        'version': 1,
        'formatters': {
            'standard': {
                'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s'
            }
        },
        'handlers': {
            'myapp_handler': {
                'class': 'logging.handlers.TimedRotatingFileHandler',
                'filename': './log/my_app.log',
                'when': 'd',
                'interval': 1,
                'backupCount': 10,
                'level': 'DEBUG',
                "encoding": "utf8",
                'formatter': 'standard'
            },
        },
        'loggers': {
            'simple': {
                'level': 'DEBUG',
                'handlers': ['myapp_handler']
            }
        },
        })

        console = logging.StreamHandler(sys.stdout)
        console.setLevel(logging.INFO)
        self.logger = logging.getLogger("simple")
        self.logger.addHandler(console)

    def getLogger(self):
        return self.logger
