import logging

def setup_custom_logger(name, log_file='project.log'):
    """
    Configure and get a custom logger.

    Parameters:
    name (str): Name of the logger.
    log_file (str): File path for logging.

    Returns:
    Logger: A configured logger.
    """
    formatter = logging.Formatter(fmt='%(asctime)s - %(levelname)s - %(module)s - %(message)s')

    handler = logging.FileHandler(log_file)
    handler.setFormatter(formatter)

    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    logger.addHandler(handler)
    return logger
