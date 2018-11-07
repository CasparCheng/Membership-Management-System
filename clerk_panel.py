#!/usr/bin/env python3

from inp_helper import (
    inp_item_name,
)
from db_helper import (
    qry_item,
    qry_all_items,
)


def clerk_list_item():
    '''
    '''
    item_name = inp_item_name()
    print()
    item = qry_item(item_name)
    if not item:
        print('\tItem not found')
        return
    item_name, item_descr, item_price = item
    print('\tName: {}'.format(item_name))
    print('\tDescr: {}'.format(item_descr))
    print('\tPrice: {}'.format(item_price))


def clerk_list_all_items():
    '''
    '''
    items = qry_all_items()
    if not items:
        print('\tNo items available')
        return
    for i, item in enumerate(items):
        ind = '[{}]'.format(i + 1)
        padding = len(ind) * ' '
        item_name, item_descr, item_price = item
        print('\t{} Name: {}'.format(ind, item_name))
        print('\t{} Descr: {}'.format(padding, item_descr))
        print('\t{} Price: {}\n'.format(padding, item_price))
