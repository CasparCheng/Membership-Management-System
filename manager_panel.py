#!/usr/bin/env python3

from inp_helper import (
    get_opt,
    inp_item_name,
    inp_item_descr,
    inp_item_price,
    inp_username,
    inp_password,
)
from db_helper import (
    qry_all_items,
    qry_item,
    add_item,
    upd_item_descr,
    upd_item_price,
    del_item,
    qry_staff,
    qry_clerk,
    qry_all_clerks,
    upd_staff_password,
    add_staff,
    del_staff,
)


def manager_manage_items_menu_1():
    ''' Display menu for managing items (1/2)
    '''
    print(
    '''
--------- Manager Panel - Manage Items ---------

    [1] -- List Item by Item Name --
    [2] -- List All Items --
    [x] -- Go Back --
    '''
    )
    return get_opt('123x')


def manager_manage_items_menu_2():
    ''' Display menu for managing items (2/2)
    '''
    print(
    '''
--------- Manager Panel - Manage Items ---------

    [1] -- Modify Item Description --
    [2] -- Modify Item Price --
    [3] -- Delete Clerk --
    [x] -- Go Back --
    '''
    )
    return get_opt('123x')


def manager_add_item():
    ''' Add an item
    '''
    while True:
        item_name = inp_item_name()
        item = qry_item(item_name)
        if item:
            print('\tDuplicated item name')
            input('\nPress enter to continue...')
            print()
            continue
        break
    item_descr = inp_item_descr()
    item_price = inp_item_price()
    print()
    add_item(item_name, item_descr, item_price)
    print('\tName: {}'.format(item_name))
    print('\tDescr: {}'.format(item_descr))
    print('\tPrice: {}'.format(item_price))


def manager_manage_items():
    ''' Manage items
    '''
    while True:
        opt = manager_manage_items_menu_1()
        print()
        if opt == '1':
            item_name = inp_item_name()
            print()
            item = qry_item(item_name)
            if not item:
                print('\tNo such item')
                input('\nPress enter to continue...')
                print()
                continue
            items = [item]
        elif opt == '2':
            items = qry_all_items()
            if not items:
                print('\tNo items available')
                input('\nPress enter to continue...')
                print()
                continue
        else:
            break

        while True:
            options = []
            for i, item in enumerate(items):
                options.append(str(i + 1))
                ind = '[{}]'.format(i + 1)
                padding = len(ind) * ' '
                item_name, item_descr, item_price = item
                print('\t{} Name: {}'.format(ind, item_name))
                print('\t{} Descr: {}'.format(padding, item_descr))
                print('\t{} Price: {}\n'.format(padding, item_price))
            print('\t[x] -- Go Back --\n')
            options += ['x']
            opt = get_opt(options)
            if opt == 'x':
                break

            item_name, item_descr, item_price = items[int(opt) - 1]

            opt = manager_manage_items_menu_2()
            print()
            if opt == '1':
                item_descr = inp_item_descr()
                print()
                upd_item_descr(item_name, item_descr)
                print('\tName: {}'.format(item_name))
                print('\tDescr: {}'.format(item_descr))
                print('\tPrice: {}'.format(item_price))
            elif opt == '2':
                item_price = inp_item_price()
                print()
                upd_item_price(item_name, item_price)
                print('\tName: {}'.format(item_name))
                print('\tDescr: {}'.format(item_descr))
                print('\tPrice: {}'.format(item_price))
            elif opt == '3':
                del_item(item_name)
                print('\tItem deleted')
            if opt not in 'x':
                input('\nPress enter to continue...')
                print()
            break


def manager_manage_clerks_menu_1():
    ''' Display menu for managing clerks (1/2)
    '''
    print(
    '''
--------- Manager Panel - Manage Clerks ---------

    [1] -- List Clerk by Username --
    [2] -- List All Clerks --
    [x] -- Go Back --
    '''
    )
    return get_opt('12x')


def manager_manage_clerks_menu_2():
    ''' Display menu for managing clerks (2/2)
    '''
    print(
    '''
--------- Manager Panel - Manage Clerks ---------

    [1] -- Modify Clerk Password --
    [2] -- Delete Clerk --
    [x] -- Go Back --
    '''
    )
    return get_opt('12x')


def manager_add_clerk():
    ''' Add a clerk
    '''
    while True:
        username = inp_username()
        staff = qry_staff(username)
        if staff:
            print('\tDuplicated username')
            input('\nPress enter to continue...')
            print()
            continue
        break
    password = inp_password()
    print()
    add_staff(username, password, 0)
    print('\tUsername: {}'.format(username))
    print('\tPassword: {}'.format(password))


def manager_manage_clerks():
    ''' Manage clerks
    '''
    while True:
        opt = manager_manage_clerks_menu_1()
        print()
        if opt == '1':
            username = inp_username()
            print()
            clerk = qry_clerk(username)
            if not clerk:
                print('\tNo such clerk')
                input('\nPress enter to continue...')
                print()
                continue
            clerks = [clerk]
        elif opt == '2':
            clerks = qry_all_clerks()
            if not clerks:
                print('\tNo clerks available')
                input('\nPress enter to continue...')
                print()
                continue
        else:
            break

        while True:
            options = []
            for i, clerk in enumerate(clerks):
                options.append(str(i + 1))
                ind = '[{}]'.format(i + 1)
                padding = len(ind) * ' '
                username, password, _ = clerk
                print('\t{} Username: {}'.format(ind, username))
                print('\t{} Password: {}\n'.format(padding, password))
            print('\t[x] -- Go Back --\n')
            options += ['x']
            opt = get_opt(options)
            if opt == 'x':
                break

            username, password, _ = clerks[int(opt) - 1]

            opt = manager_manage_clerks_menu_2()
            print()
            if opt == '1':
                password = inp_password()
                print()
                upd_staff_password(username, password)
                print('\tUsername: {}'.format(username))
                print('\tPassword: {}'.format(password))
            elif opt == '2':
                del_staff(username)
                print('\tClerk deleted')
            if opt not in 'x':
                input('\nPress enter to continue...')
                print()
            break
