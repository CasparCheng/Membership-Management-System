#!/usr/bin/env python3

from db_helper import init_conn, create_tables, add_admin
from inp_helper import get_opt
from login import member_login, staff_login
from panel import member_panel, clerk_panel, manager_panel


def menu():
    ''' Dispaly main menu
    '''
    print(
    '''
--------- Main Menu ---------

    [1] -- Member --
    [2] -- Clerk --
    [3] -- Manager --
    [x] -- Quit --
    '''
    )
    return get_opt('123x')


def main():
    ''' Main procedure
    '''
    while True:
        opt = menu()
        print()
        if opt == '1':
            member = member_login()
            if member:
                member_panel(member)
        elif opt in '2':
            clerk = staff_login()
            if clerk:
                clerk_panel(clerk)
        elif opt in '3':
            manager = staff_login(True)
            if manager:
                manager_panel(manager)
        else:
            return


if __name__ == '__main__':
    with init_conn('database.db'):
        create_tables()
        add_admin()
        main()
