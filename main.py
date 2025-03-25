import logging


def export_log(text: str):
    """ Export log
    """

    # create logger
    logger = logging.getLogger('my_logger')
    logger.setLevel(logging.INFO)

    # create file handler
    file_handler = logging.FileHandler('app.log')
    file_handler.setLevel(logging.INFO)

    # create console handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)

    # set log format
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    # add handlers to logger
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    # log
    logger.error(text)

    return


if __name__ == '__main__':
    export_log('Hello, World!')
