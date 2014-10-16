#!usr/bin/env python
# -*- coding: utf-8 -*-
""" Task 09: Merging Data Using a Dictionary Key """

import task_09_utility
from pprint import pprint

DATA_FILES = [
    {
        'data': 'task_09_data/router_01.csv'
    },
    {
        'data': 'task_09_data/router_02.csv'
    },
    {
        'data': 'task_09_data/router_03.csv'
    }
]


def load_data(data):
    """load data"""

    key_value = 0
    loaded_data = {}
    for item in data:
        key_value += 1
        value = task_09_utility.get_data(item['data'])
        loaded_data[key_value] = value

    return loaded_data


DATA = load_data(DATA_FILES)
print DATA


def merge_data(loaded_data):
    """merge data"""

    merged_data = {}
    for key, value in loaded_data.iteritems():
        for traffic in value:
            candidate_key = traffic['clock'][8:13]

            if candidate_key not in merged_data:
                merged_data[candidate_key] = [traffic.get('clock'), 0, 0, 0]

            merged_data[candidate_key][key] = traffic.get('value_avg')

    sorted_data = task_09_utility.sort_dict(merged_data)
    return sorted_data

SORTED_LIST = merge_data(DATA)
pprint(SORTED_LIST)