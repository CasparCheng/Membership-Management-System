#!/usr/bin/env python3

import re
from datetime import datetime


def get_opt(options):
    ''' Get input option
    '''
    while True:
        opt = input('Please choose: ')
        if opt not in options:
            continue
        return opt


def inp_username():
    ''' Get input username
    '''
    while True:
        username = input('Please input username [3~8 chars]: ')
        if not username or len(username) < 3 or len(username) > 8:
            print('\tUsername must contain 3~8 characters')
            continue
        return username


def inp_password():
    ''' Get input password
    '''
    while True:
        password = input('Please input password [3~8 chars]: ')
        if not password or len(password) < 3 or len(password) > 8:
            print('\tPassword must contain 3~8 characters')
            continue
        return password


def inp_card_no():
    ''' Get input card No.
    '''
    while True:
        card_no = input('Please input card NO. [6 digits]: ')
        if not card_no or len(card_no) != 6 or not card_no.isdigit():
            print('\tCard NO. must contain exactly 6 digits')
            continue
        return int(card_no)


def inp_name():
    ''' Get input name
    '''
    while True:
        name = input('Please input your name [>1 chars]: ')
        if not name or len(name) < 2:
            print('\tName must contain more than 1 character')
            continue
        return name


def inp_gender():
    ''' Get input gender
    '''
    while True:
        gender = input('Please input your gender [M/F]: ')
        if not gender or len(gender) != 1 or gender not in 'MF':
            print('\tGender must be either "M" or "F"')
            continue
        return gender


def inp_phone():
    ''' Get input phone No.
    '''
    while True:
        phone = input('Please input your phone number [11 digits]: ')
        if not phone or len(phone) != 11 or not phone.isdigit():
            print('\tPhone number must contain exactly 11 digits')
            continue
        return phone


def inp_email():
    ''' Get input email
    '''
    while True:
        email = input('Please input your email number (optional): ')
        if email and not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            print('\tEmail address must be in format of x@x.x')
            continue
        return email


def inp_address():
    ''' Get input address
    '''
    while True:
        address = input('Please input your address [>1 chars]: ')
        if not address or len(address) < 2:
            print('\tAddress must contain more than 1 character')
            continue
        return address


def inp_money():
    ''' Get input money
    '''
    while True:
        money = input('Please input the amount [>=0.01]: ')
        if not money:
            print('\tAmount of money must be positive number')
            continue
        try:
            money = float(money)
        except ValueError:
            print('\tAmount of money must be >= 0.01')
            continue
        if money < 0.01:
            print('\tAmount of money must be >= 0.01')
            continue
        money = round(money, 2)
        return money


def inp_item_name():
    ''' Get input item name
    '''
    while True:
        item_name = input('Please input the item name [>1 chars]: ')
        if not item_name or len(item_name) < 2:
            print('\tItem name must contain more than 1 character')
            continue
        return item_name


def inp_date():
    ''' Get input date
    '''
    while True:
        date = input('Please input the date [YYYY-MM-DD]: ')
        if not date:
            print('\tDate must be in format of YYYY-MM-DD')
            continue
        try:
            datetime.strptime(date, '%Y-%m-%d')
        except ValueError:
            print('\tDate must be in format of YYYY-MM-DD')
            continue
        return date


def inp_item_descr():
    ''' Get input item description
    '''
    while True:
        item_descr = input('Please input the item description [>1 chars]: ')
        if not item_descr or len(item_descr) < 2:
            print('\tItem description must contain more than 1 character')
            continue
        return item_descr


def inp_item_price():
    ''' Get input item price
    '''
    while True:
        item_price = input('Please input the item price [>=0.01]: ')
        if not item_price:
            print('\tItem price must be number >= 0.01')
            continue
        try:
            item_price = float(item_price)
        except ValueError:
            print('\tItem price must be number >= 0.01')
            continue
        if item_price < 0.01:
            print('\tItem price must be number >= 0.01')
            continue
        item_price = round(item_price, 2)
        return item_price
