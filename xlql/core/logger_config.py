import logging

def setup_logger(level=logging.INFO):

    console_handler = logging.StreamHandler()
    console_handler.setLevel(level)

    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    console_handler.setFormatter(formatter)

    logger = logging.getLogger('GlobalLogger')
    logger.setLevel(level)

    if not logger.handlers:
        logger.addHandler(console_handler)
    return logger

logger = setup_logger()