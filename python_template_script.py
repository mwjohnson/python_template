#!/usr/bin/env python
# -*- coding: utf-8 -*-
import logging
from timeit import default_timer
import functools
import configparser


logging.basicConfig()
logger = logging.getLogger(__name__)
logger.setLevel(level=logging.INFO)


def timer_decorator(func_to_time):
    """
    A timer decorator. Using this, like in the load_settings() function declaration below will enable a timing
    report for the function call.
    Simply include @timer_decorator before you function definition.
    @timer_decorator
    def my_timed_function():
    :param func_to_time: the function to measure the time of execution.
    :return: the wrapper - used for decoration.
    """
    @functools.wraps(func_to_time)
    def wrapper_timer(*args, **kwargs):
        start = default_timer()
        result = func_to_time(*args, **kwargs)
        end = default_timer()
        logger.info(func_to_time.__name__ + ': elapsed time: %s', end - start)
        return result

    return wrapper_timer


@timer_decorator
def load_settings():
    """
    Load settings from the input-file, config.ini
    Example settings which can be placed inside the settings dictionary.

    'string_setting': cfg.get('settings', 'some_string_setting'),
    'Integer_setting': cfg.getint('settings', 'integer_config_setting'),
    'float_setting': cfg.getfloat('settings', 'float_config_setting'),
    'boolean_setting': cfg.getboolean('settings', 'boolean_config'),

    :return: the settings dictionary.
    """
    cfg = configparser.ConfigParser()
    cfg.read_file(open('config.ini'))

    settings = {

    }

    return settings


def main():
    logger.info(__name__ + " started.")

    logger.info('Complete.')


if __name__ == '__main__':
    main()
