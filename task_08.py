#!usr/bin/env python
# -*- coding: utf-8 -*-
""" Task 08: Dictionary Comprehensions """

from data import FRUIT
print FRUIT


shoplist = {
    'Lime': 12,
    'Red Pear': 4,
    'Peach': 24,
    'Beet': 1,
    }


def get_cost_per_item(shop_list):
    """get cost per item on shopping list"""
    cost_list = {item: shop_list[item] * FRUIT[item] for item in shop_list.keys() if item in FRUIT}
    return cost_list

COST_PER_ITEM = get_cost_per_item(shoplist)
print COST_PER_ITEM


def get_total_cost(shop_list):
    """gets total cost"""

    total_cost = sum(get_cost_per_item(shop_list).values())
    return total_cost

TOTAL_COST = get_total_cost(shoplist)
print TOTAL_COST