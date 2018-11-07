#!/usr/bin/env python3

from inp_helper import (
    get_opt,
    inp_money,
    inp_item_name,
)
from db_helper import (
    upd_member_balance,
    del_member,
    qry_item,
    qry_all_items,
    add_transaction,
    qry_transactions_by_card_no,
)


def member_account_info(member):
    ''' Show account info
    '''
    card_no, password, name, gender, phone, email, address, balance = member
    print('\tYour account info:')
    print('\t----------------------------')
    print('\tCard No.: {}'.format(card_no))
    print('\tPassword: {}'.format(password))
    print('\tName: {}'.format(name))
    print('\tGender: {}'.format(gender))
    print('\tPhone: {}'.format(phone))
    print('\tEmail: {}'.format(email))
    print('\tAddress: {}'.format(address))
    print('\tBalance: {}'.format(balance))


def member_recharge(member):
    ''' Recharge card
    '''
    card_no, _, _, _, _, _, _, balance = member
    money = inp_money()
    print()
    balance += money
    upd_member_balance(card_no, balance)
    member[7] = balance
    print('\tYour balance: {}'.format(balance))


def member_purchase_items_menu():
    ''' Display menu for purchasing items
    '''
    print(
    '''
--------- Member Panel - Purchase Items ---------

    [1] -- List Item by Item Name --
    [2] -- List All Items --
    [x] -- Go Back --
    '''
    )
    return get_opt('12x')


def member_purchase_items(member):
    ''' Purchase items
    '''
    opt = member_purchase_items_menu()
    print()
    if opt == '1':
        item_name = inp_item_name()
        print()
        item = qry_item(item_name)
        if not item:
            print('\tNo such item')
            return
        items = [item]
    elif opt == '2':
        items = qry_all_items()
        if not items:
            print('\tNo items available')
            return
    else:
        return

    card_no, _, _, _, _, _, _, balance = member
    while True:
        options = []
        for i, item in enumerate(items):
            options.append(str(i + 1))
            ind = '[{}]'.format(i + 1)
            item_name, item_descr, item_price = item
            print('\t{} Name: {}'.format(ind, item_name))
            print('\t{} Descr: {}'.format(len(ind) * ' ', item_descr))
            print('\t{} Price: {}\n'.format(len(ind) * ' ', item_price))
        print('\t[x] -- Go Back --\n')
        options += ['x']
        opt = get_opt(options)
        if opt == 'x':
            break

        item_name, _, item_price = items[int(opt) - 1]
        if item_price > balance:
            print('\tYour balance is not enough')
        else:
            balance -= item_price
            add_transaction(card_no, item_name, item_price)
            upd_member_balance(card_no, balance)
            member[6] = balance
            print('\tYour have purchased {} at {}'.format(item_name, item_price))
            print('\tYour balance: {}'.format(balance))
        input('\nPress enter to continue...')
        print()


def member_transactions(member):
    ''' Show transactions
    '''
    card_no, _, _, _, _, _, _, _ = member
    transactions = qry_transactions_by_card_no(card_no)
    if not transactions:
        print('\tNo transactions found')
        return
    expenditure = 0
    for transaction in transactions:
        _, _, item_name, item_price, date = transaction
        print('\t[{}] {} at {}'.format(date, item_name, item_price))
        expenditure += item_price
    print('\n\tTotal Expenditure: {}'.format(expenditure))


def member_return_card(member):
    ''' Return card
    '''
    card_no, _, _, _, _, _, _, balance = member
    del_member(card_no)
    print('\tHere is the refund: {}'.format(balance))
