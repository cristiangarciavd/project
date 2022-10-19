"""Custom logger for the project"""
import logging
import logging.config


@staticmethod
def get_logger(name='appLogger'):
    """Get logger method"""
    try:
        logging.config.fileConfig("./log.ini")
        logger = logging.getLogger(name)
    except Exception("log.ini doesn't found"):
        log_file = 'main/logger/logfile.log'
        log_lvl = logging.INFO
        format = "%(asctime)-15s %(levelname)-8s %(message)s"
        logging.basicConfig(level=log_lvl, filename=log_file, filemode="w+",
                            format=format)
        logger = logging.getLogger(name)
    return logger


def wrap(pre, post):
    """ Wrapper """
    def decorate(func):
        """ Decorator """
        def call(*args, **kwargs):
            """ Actual wrapping """
            pre(func)
            result = func(*args, **kwargs)
            post(func)
            return result
        return call
    return decorate


def entering(func, *args):
    """ Pre function logging """
    logger = get_logger('appLogger')
    logger.debug("Entered %s", func.__name__)
    logger.info(func.__doc__)
    logger.debug("Function at line %d in %s" %
                 (func.__code__.co_firstlineno, func.__code__.co_filename))


def exiting(func):
    """ Post function logging """
    get_logger().debug("Exited  %s", func.__name__)
