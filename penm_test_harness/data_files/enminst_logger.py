#!/usr/bin/env python
import logging
logging.basicConfig(filename="/var/log/enminst.log",
                    format='%(asctime)s %(levelname)s %(message)s',
                    filemode='w')
logger=logging.getLogger()

def init_enminst_logging():
    logger.setLevel(logging.INFO)
    logger.info("MOCK ENMinst log")


def log_header(_, message):
    logger.info('-' * 65)
    logger.info(message)
    logger.info('-' * 65)

