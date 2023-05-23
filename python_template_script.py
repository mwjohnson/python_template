#!/usr/bin/env python
# -*- coding: utf-8 -*-
import csv
import logging
import os
from timeit import default_timer
import functools
import configparser


logging_format = "Module: %(name)s\tFilename: %(filename)s:%(lineno)d\tFunction: %(funcName)s" \
                 "\n\t%(levelname)s: %(message)s"
logging.basicConfig(format=logging_format)  # 標準出力のフォーマットは、loggingで設定
logger = logging.getLogger(__name__)
logger.setLevel(level=logging.DEBUG)
file_sh = logging.FileHandler('./debug.log')  # ログファイルに出力するHandlerの設定
file_sh.setFormatter(logging.Formatter(logging_format))
logger.addHandler(file_sh)



def write_dictionary_to_json_file(filename, dict_data):
    """
    Write a dictionary to a json file.
    :param filename: file path to be written.
    :param dict_data: data to be written.
    :return:
    """
    with open(filename, 'w', encoding='utf8') as fp:
        json.dump(dict_data, fp)
    logging.info(f'{filename} has been written to file.')


def load_json_file_to_dict(filename):
    """
    Read a json file into a dictionary data-structure.
    :param filename: file path of the file to read.
    :return: dictionary object containing the data
    """
    assert os.path.isfile(filename), f'{filename} is not a file.'
    with open(filename, encoding='utf8') as fp:
        data = json.load(fp)
    logging.info(f'{filename} has been read in as data.')
    return data


def write_output(data, field_names, file_output_path):
    """
    Write data to csv file.

    :param data: the data to write to file.
    :param field_names: the column names.
    :param file_output_path: the file to write to.
    :return: None.
    """
    with open(file_output_path, 'w', encoding='utf8', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=field_names)
        writer.writeheader()
        writer.writerows(data)
    logger.info(f'file written: {file_output_path}')


def read_in_lines(input_file_path):
    """
    Read in the csv file, file_path.

    :param input_file_path: the filepath to read in.
    :return: field_names and the data.
    """
    field_names = None
    assert os.path.isfile(input_file_path), f'Missing file. Checking path: {os.path.abspath(input_file_path)}'
    with open(input_file_path, mode='r', encoding='utf8') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        field_names = csv_reader.fieldnames
        lines = [row for row in csv_reader]
    logger.info(f'Read in file: {input_file_path}')
    return field_names, lines


def read_csv(input_file_path):
    """
    Read a csv file in and return a list of data.

    :param input_file_path: file path of the file to be read in.
        Example: input_file_path = 'path/to/file/my_csv_file.csv'
    :return: a list of data.
    """
    assert os.path.isfile(input_file_path), f'Missing file. Checking path: {os.path.abspath(input_file_path)}'
    with open(input_file_path, newline='', encoding='utf8') as csv_file:
        reader = csv.DictReader(csv_file, dialect=csv.excel_tab)
        data = [r for r in reader]
    logger.info(f'Read in file: {input_file_path}')
    return data


def write_list_of_dictionaries_to_csv(file_path, data):
    """
    Write a list of dictionaries to a csv file.

    :param file_path: the filepath to write to.
    :param data: the dictionary data to write to file.

    Example:
    data = [
        {'key1': 0, 'column2': 'abc', 'key3': 1},
        {'key1': 1, 'column2': 'def', 'key3': 3}
    ]

    File output:
        key1, column2, key3
        0,abc,1
        1,def,3

    :return: None
    """
    with open(file_path, 'w', encoding='utf8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=data.keys())
        writer.writeheader()
        writer.writerows(data)
    logger.info(f'{file_path} written.')


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
