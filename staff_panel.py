#!/usr/bin/env python3

from inp_helper import (
    inp_item_name,
    inp_card_no,
    inp_phone,
    inp_date,
)
from db_helper import (
    qry_member,
    qry_member_by_phone,
    qry_all_members,
    qry_transactions_by_card_no,
    qry_transactions_by_item_name,
    qry_transactions_by_date,
    qry_all_transactions,
)


def staff_account_info(staff):
    ''' Show account info
    '''
    username, _, is_manager = staff
    print('\tYour account info:')
    print('\t----------------------------')
    print('\tUsername: {}'.format(username))
    print('\tPosition: {}'.format('Manager' if is_manager else 'Clerk'))


def staff_list_member():
    ''' List member by card No.
    '''
    card_no = inp_card_no()
    print()
    member = qry_member(card_no)
    if not member:
        print('\tInvalid card No.')
        return
    card_no, password, name, gender, phone, email, address, balance = member
    print('\tMember account info:')
    print('\t----------------------------')
    print('\tCard No.: {}'.format(card_no))
    print('\tPassword: {}'.format(password))
    print('\tName: {}'.format(name))
    print('\tGender: {}'.format(gender))
    print('\tPhone: {}'.format(phone))
    print('\tEmail: {}'.format(email))
    print('\tAddress: {}'.format(address))
    print('\tBalance: {}'.format(balance))


def staff_list_member_by_phone():
    ''' List member by phone
    '''
    phone = inp_phone()
    print()
    member = qry_member_by_phone(phone)
    if not member:
        print('\tInvalid Phone No.')
        return
    card_no, password, name, gender, phone, email, address, balance = member
    print('\tMember account info:')
    print('\t----------------------------')
    print('\tCard No.: {}'.format(card_no))
    print('\tPassword: {}'.format(password))
    print('\tName: {}'.format(name))
    print('\tGender: {}'.format(gender))
    print('\tPhone: {}'.format(phone))
    print('\tEmail: {}'.format(email))
    print('\tAddress: {}'.format(address))
    print('\tBalance: {}'.format(balance))


def staff_list_all_members():
    ''' List all members
    '''
    members = qry_all_members()
    if not members:
        print('\tNo members available')
        return
    for i, member in enumerate(members):
        ind = '[{}]'.format(i + 1)
        padding = len(ind) * ' '
        card_no, password, name, gender, phone, email, address, balance = member
        print('\t{} Card No.: {}'.format(ind, card_no))
        print('\t{} Password: {}'.format(padding, password))
        print('\t{} Name: {}'.format(padding, name))
        print('\t{} Gender: {}'.format(padding, gender))
        print('\t{} Phone: {}'.format(padding, phone))
        print('\t{} Email: {}'.format(padding, email))
        print('\t{} Address: {}'.format(padding, address))
        print('\t{} Balance: {}\n'.format(padding, balance))


def staff_list_transactions_by_card_no():
    ''' List transactions by card No.
    '''
    card_no = inp_card_no()
    print()
    transactions = qry_transactions_by_card_no(card_no)
    if not transactions:
        print('\tNo transactions found')
        return
    income = 0
    for i, transaction in enumerate(transactions):
        _, card_no, item_name, item_price, date = transaction
        print('\t[{}] Owner of card No.: {} purchased {} at {} on {}'.format(
            i + 1, card_no, item_name, item_price, date))
        income += item_price
    print('\n\tTotal Income: {}'.format(income))


def staff_list_transactions_by_item_name():
    ''' List transactions by item name
    '''
    item_name = inp_item_name()
    print()
    transactions = qry_transactions_by_item_name(item_name)
    if not transactions:
        print('\tNo transactions found')
        return
    income = 0
    for i, transaction in enumerate(transactions):
        _, card_no, item_name, item_price, date = transaction
        print('\t[{}] Owner of card No.: {} purchased {} at {} on {}'.format(
            i + 1, card_no, item_name, item_price, date))
        income += item_price
    print('\n\tTotal Income: {}'.format(income))


def staff_list_transactions_by_date():
    ''' List transactions by date
    '''
    date = inp_date()
    print()
    transactions = qry_transactions_by_date(date)
    if not transactions:
        print('\tNo transactions found')
        return
    income = 0
    for i, transaction in enumerate(transactions):
        _, card_no, item_name, item_price, date = transaction
        print('\t[{}] Owner of card No.: {} purchased {} at {} on {}'.format(
            i + 1, card_no, item_name, item_price, date))
        income += item_price
    print('\n\tTotal Income: {}'.format(income))


def staff_list_all_transactions():
    ''' List all transactions
    '''
    transactions = qry_all_transactions()
    if not transactions:
        print('\tNo transactions found')
        return
    income = 0
    for i, transaction in enumerate(transactions):
        _, card_no, item_name, item_price, date = transaction
        print('\t[{}] Owner of card No.: {} purchased {} at {} on {}'.format(
            i + 1, card_no, item_name, item_price, date))
        income += item_price
    print('\n\tTotal Income: {}'.format(income))
