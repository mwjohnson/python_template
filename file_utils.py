#!/usr/bin/env python
# -*- coding: utf-8 -*-
import csv
import json
import os
from logger import setup_custom_logger


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


def write_list_of_dictionaries_to_csv(file_output_path, data):
    """
    Write a list of dictionaries to a csv file.

    :param file_output_path: the filepath to write to.
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
    with open(file_output_path, 'w', encoding='utf8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=data.keys())
        writer.writeheader()
        writer.writerows(data)
    logger.info(f'file written: {file_output_path}')


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