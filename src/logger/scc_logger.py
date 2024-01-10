import logging
import os
from datetime import datetime


def setupSCCLogger(log_file, debug=False, log=True):
    if debug:
        logging.basicConfig(filename=log_file,
                            level=logging.DEBUG,
                            filemode="a",
                            datefmt='%m-%d-%Y %I:%M:%S-%p',
                            format='[%(asctime)s-DEBUGGER]%(message)s')
    elif log:
        logging.basicConfig(filename=log_file,
                            level=logging.INFO,
                            filemode="a",
                            datefmt='%m-%d-%Y %I:%M:%S %p',
                            format='[%(asctime)s]%(message)s')
    else:
        logging.basicConfig(filename=log_file,
                            level=logging.WARNING,
                            filemode="r",
                            datefmt='%m-%d-%Y %I:%M:%S %p',
                            format='[%(asctime)s]%(message)s')


def info(msg):
    print("[" + datetime.today().replace(microsecond=0).isoformat(' ') + "][SCC-INFO]: " + msg)
    logging.info("[SCC-INFO]: " + msg)


def debug(msg):
    print("[" + datetime.today().replace(microsecond=0).isoformat(' ') + "][SCC-DEBUG]: " + msg)
    logging.debug("[SCC-DEBUG]: " + msg)


def error(msg):
    print("[" + datetime.today().replace(microsecond=0).isoformat(' ') + "][SCC-ERROR]: " + msg)
    logging.error("[SCC-ERROR]: " + msg)


def fatal(msg):
    print("[" + datetime.today().replace(microsecond=0).isoformat(' ') + "][SCC-CRITICAL]: " + msg)
    logging.critical("[SCC-CRITICAL]: " + msg)