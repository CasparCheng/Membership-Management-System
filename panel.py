#!/usr/bin/env python3

from inp_helper import (
    get_opt,
)
from member_panel import (
    member_account_info,
    member_recharge,
    member_purchase_items,
    member_transactions,
    member_return_card,
)
from staff_panel import (
    staff_account_info,
    staff_list_member,
    staff_list_member_by_phone,
    staff_list_all_members,
    staff_list_transactions_by_card_no,
    staff_list_transactions_by_item_name,
    staff_list_transactions_by_date,
    staff_list_all_transactions,
)
from clerk_panel import (
    clerk_list_item,
    clerk_list_all_items,
)
from manager_panel import (
    manager_manage_items,
    manager_manage_clerks,
    manager_add_item,
    manager_add_clerk,
)


def member_panel_menu():
    ''' Display member panel menu
    '''
    print(
    '''
--------- Member Panel ---------

    [0] -- Account Info --
    [1] -- Recharge Card --
    [2] -- Purchase Items --
    [3] -- Transactions --
    [4] -- Return Card
    [x] -- Logout --
    '''
    )
    return get_opt('01234x')


def member_panel(member):
    ''' Carry out member panel operations
    '''
    member = list(member)
    card_no, password, name, gender, phone, email, address, balance = member
    print('\tYour card No.: {}'.format(card_no))
    print('\tYour balance: {}'.format(balance))
    while True:
        opt = member_panel_menu()
        print()
        if opt == '0':
            member_account_info(member)
        elif opt == '1':
            member_recharge(member)
        elif opt == '2':
            member_purchase_items(member)
        elif opt == '3':
            member_transactions(member)
        elif opt == '4':
            member_return_card(member)
        if opt in '4x':
            print('\tYour are logged out...')
            break
        if opt not in '2':
            input('\nPress enter to continue...')
            print()


def clerk_panel_menu():
    ''' Display clerk panel menu
    '''
    print(
    '''
--------- Clerk Panel ---------

    [0] -- Account Info --
    [1] -- List Member by Card No. --
    [2] -- List Member by Phone No. --
    [3] -- List All Members --
    [4] -- List Transactions by Card NO. --
    [5] -- List Transactions by Item Name --
    [6] -- List Transactions by Date --
    [7] -- List All Transactions --
    [8] -- List Item by Name --
    [9] -- List All Items --
    [x] -- Logout --
    '''
    )
    return get_opt('0123456789x')


def clerk_panel(clerk):
    ''' Carry out clerk panel operations
    '''
    clerk = list(clerk)
    while True:
        opt = clerk_panel_menu()
        print()
        if opt == '0':
            staff_account_info(clerk)
        elif opt == '1':
            staff_list_member()
        elif opt == '2':
            staff_list_member_by_phone()
        elif opt == '3':
            staff_list_all_members()
        elif opt == '4':
            staff_list_transactions_by_card_no()
        elif opt == '5':
            staff_list_transactions_by_item_name()
        elif opt == '6':
            staff_list_transactions_by_date()
        elif opt == '7':
            staff_list_all_transactions()
        elif opt == '8':
            clerk_list_item()
        elif opt == '9':
            clerk_list_all_items()
        else:
            print('\tYour are logged out...')
            break
        input('\nPress enter to continue...')
        print()


def manager_panel_menu():
    ''' Display manager panel menu
    '''
    print(
    '''
--------- Manager Panel ---------

    [0]  -- Account Info --
    [1]  -- List Member by Card No. --
    [2]  -- List Member by Phone No. --
    [3]  -- List All Members --
    [4]  -- List Transactions by Card NO. --
    [5]  -- List Transactions by Item Name --
    [6]  -- List Transactions by Date --
    [7]  -- List All Transactions --
    [8]  -- Add Item --
    [9]  -- Manage Items --
    [10] -- Add Clerk --
    [11] -- Manage Clerks --
    [x]  -- Logout --
    '''
    )
    return get_opt(('1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', 'x'))


def manager_panel(manager):
    ''' Carry out manager panel operations
    '''
    manager = list(manager)
    while True:
        opt = manager_panel_menu()
        print()
        if opt == '0':
            staff_account_info(manager)
        elif opt == '1':
            staff_list_member()
        elif opt == '2':
            staff_list_member_by_phone()
        elif opt == '3':
            staff_list_all_members()
        elif opt == '4':
            staff_list_transactions_by_card_no()
        elif opt == '5':
            staff_list_transactions_by_item_name()
        elif opt == '6':
            staff_list_transactions_by_date()
        elif opt == '7':
            staff_list_all_transactions()
        elif opt == '8':
            manager_add_item()
        elif opt == '9':
            manager_manage_items()
        elif opt == '10':
            manager_add_clerk()
        elif opt == '11':
            manager_manage_clerks()
        else:
            print('\tYour are logged out...')
            break
        if opt not in ('9', '11', 'x'):
            input('\nPress enter to continue...')
            print()
