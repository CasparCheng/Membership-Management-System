#!/usr/bin/env python3

from random import choice
from string import (
    ascii_letters,
    digits
)
from db_helper import (
    qry_member, qry_member_by_phone, qry_last_member, add_member,
    qry_staff
)
from inp_helper import (
    get_opt,
    inp_username, inp_password, inp_card_no,
    inp_name, inp_gender, inp_phone, inp_email, inp_address
)

CHARS = ascii_letters + digits + '!@#$%^&*()'

CARD_NO_BASE = 100000


def member_login_menu():
    ''' Show login menu for member
    '''
    print(
    '''
--------- Member Login ---------

    [1] -- Login --
    [2] -- Register --
    [x] -- Go Back --
    '''
    )
    return get_opt('12x')


def staff_login_menu():
    ''' Show login menu for staff
    '''
    print(
    '''
--------- Staff Login ---------

    [1] -- Login --
    [x] -- Go Back --
    '''
    )
    return get_opt('1x')


def gen_card_no():
    ''' Generate card No.
    '''
    row = qry_last_member()
    if not row:
        return CARD_NO_BASE
    return row[0] + 1


def gen_password():
    ''' Generate password
    '''
    return ''.join(choice(CHARS) for i in range(6))


def member_login():
    ''' Login operation for member
    '''
    while True:
        opt = member_login_menu()
        print()
        if opt == '1':
            card_no = inp_card_no()
            password = inp_password()
            print()
            member = qry_member(card_no)
            if not member:
                print('\n\tInvalid Card No.')
            elif member[1] != password:
                print('\n\tInvalid password')
            else:
                print('\n\tYou are logging in...\n')
                return member
        elif opt == '2':
            card_no = gen_card_no()
            password = gen_password()
            name = inp_name()
            gender = inp_gender()
            while True:
                phone = inp_phone()
                if qry_member_by_phone(phone):
                    print('\tThis phone number already exists')
                    continue
                break
            email = inp_email()
            address = inp_address()
            print()
            balance = 0
            member = add_member(card_no, password, name, gender, phone,
                                email, address, balance)
            print('\n\tPlease make note of your card No. and password:')
            print('\tYour card No.: {}'.format(card_no))
            print('\tYour password: {}'.format(password))
            print('\n\tYou are logging in...\n')
            return member
        else:
            break


def staff_login(is_manager=False):
    ''' Login operation for staff
    '''
    while True:
        opt = staff_login_menu()
        print()
        if opt == '1':
            username = inp_username()
            password = inp_password()
            print()
            staff = qry_staff(username)
            if not staff:
                print('\n\tInvalid username')
            elif staff[1] != password:
                print('\n\tInvalid password')
            elif is_manager and staff[2] == 0:
                print('\n\tYou are not manager')
            else:
                print('\n\tYou are logging in...\n')
                return staff
        else:
            break
