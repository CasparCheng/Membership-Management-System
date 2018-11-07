#!/usr/bin/env python3

import sqlite3
from sql_tables import sql_tables
from sql_stmts import (
    sql_add_staff,
    sql_qry_staff,
    sql_qry_clerk,
    sql_qry_all_clerks,
    sql_upd_staff_password,
    sql_del_staff,
    # ----------------------------
    sql_add_member,
    sql_qry_member,
    sql_qry_member_by_phone,
    sql_qry_member_last,
    sql_upd_member_balance,
    sql_del_member,
    sql_qry_all_members,
    # ----------------------------
    sql_qry_item,
    sql_qry_all_items,
    sql_add_item,
    sql_upd_item_descr,
    sql_upd_item_price,
    sql_del_item,
    # ----------------------------
    sql_add_transaction,
    sql_qry_transactions_by_card_no,
    sql_qry_transactions_by_item_name,
    sql_qry_transactions_by_date,
    sql_qry_all_transactions,
)
from sys import exit
from datetime import datetime

CONN = None


def init_conn(filename):
    ''' Initialize database
    '''
    global CONN
    try:
        CONN = sqlite3.connect(filename)
    except sqlite3.Error as e:
        print(e)
        exit(1)
    return CONN


def create_tables():
    ''' Create database
    '''
    for table_name, sql_table in sql_tables:
        print('Creating table {} ...'.format(table_name))
        try:
            cur = CONN.cursor()
            cur.execute(
                sql_table
            )
            CONN.commit()
        except sqlite3.Error as e:
            print(e)
            exit(1)


def add_admin():
    ''' Initialize database
    '''
    try:
        cur = CONN.cursor()
        cur.execute(
            sql_qry_staff, ('admin',)
        )
        if not cur.fetchone():
            cur.execute(
                sql_add_staff, ('admin', 'pwd', 1)
            )
            CONN.commit()
    except sqlite3.Error as e:
        print(e)
        exit(1)


def qry_member(card_no):
    ''' Query a member by card No.
    '''
    try:
        cur = CONN.cursor()
        cur.execute(
            sql_qry_member, (card_no,)
        )
        return cur.fetchone()
    except sqlite3.Error as e:
        print(e)
        exit(1)


def qry_member_by_phone(phone):
    ''' Query a member by phone No.
    '''
    try:
        cur = CONN.cursor()
        cur.execute(
            sql_qry_member_by_phone, (phone,)
        )
        return cur.fetchone()
    except sqlite3.Error as e:
        print(e)
        exit(1)


def qry_last_member():
    ''' Query the last member
    '''
    try:
        cur = CONN.cursor()
        cur.execute(
            sql_qry_member_last
        )
        return cur.fetchone()
    except sqlite3.Error as e:
        print(e)
        exit(1)


def add_member(
        card_no, password, name, gender, phone, email, address, balance):
    ''' Add a member into table
    '''
    try:
        cur = CONN.cursor()
        cur.execute(
            sql_add_member,
            (card_no, password, name, gender, phone, email, address, balance)
        )
        CONN.commit()
        return (card_no, password, name, gender,
                phone, email, address, balance)
    except sqlite3.Error as e:
        print(e)
        exit(1)


def qry_staff(username):
    ''' Query a staff by username
    '''
    try:
        cur = CONN.cursor()
        cur.execute(
            sql_qry_staff, (username,)
        )
        return cur.fetchone()
    except sqlite3.Error as e:
        print(e)
        exit(1)


def upd_member_balance(card_no, balance):
    ''' Update a member's balance
    '''
    try:
        cur = CONN.cursor()
        cur.execute(
            sql_upd_member_balance, (balance, card_no)
        )
        CONN.commit()
    except sqlite3.Error as e:
        print(e)
        exit(1)


def del_member(card_no):
    ''' Delete a member
    '''
    try:
        cur = CONN.cursor()
        cur.execute(
            sql_del_member, (card_no,)
        )
        CONN.commit()
    except sqlite3.Error as e:
        print(e)
        exit(1)


def qry_item(name):
    ''' Query a item by name
    '''
    try:
        cur = CONN.cursor()
        cur.execute(
            sql_qry_item, (name,)
        )
        return cur.fetchone()
    except sqlite3.Error as e:
        print(e)
        exit(1)


def qry_all_items():
    ''' Query all items
    '''
    try:
        cur = CONN.cursor()
        cur.execute(
            sql_qry_all_items
        )
        return cur.fetchall()
    except sqlite3.Error as e:
        print(e)
        exit(1)


def add_transaction(card_no, item_name, item_price):
    ''' Add a transaction
    '''
    date = datetime.today().strftime('%Y-%m-%d')
    try:
        cur = CONN.cursor()
        cur.execute(
            sql_add_transaction, (card_no, item_name, item_price, date)
        )
        CONN.commit()
    except sqlite3.Error as e:
        print(e)
        exit(1)


def qry_transactions_by_card_no(card_no):
    ''' Query a transaction by card No.
    '''
    try:
        cur = CONN.cursor()
        cur.execute(
            sql_qry_transactions_by_card_no, (card_no,)
        )
        return cur.fetchall()
    except sqlite3.Error as e:
        print(e)
        exit(1)


def qry_all_members():
    ''' Query all members
    '''
    try:
        cur = CONN.cursor()
        cur.execute(
            sql_qry_all_members
        )
        return cur.fetchall()
    except sqlite3.Error as e:
        print(e)
        exit(1)


def qry_transactions_by_item_name(item_name):
    ''' Query transactions by item name
    '''
    try:
        cur = CONN.cursor()
        cur.execute(
            sql_qry_transactions_by_item_name, (item_name,)
        )
        return cur.fetchall()
    except sqlite3.Error as e:
        print(e)
        exit(1)


def qry_transactions_by_date(date):
    ''' Query transactions by date
    '''
    try:
        cur = CONN.cursor()
        cur.execute(
            sql_qry_transactions_by_date, (date,)
        )
        return cur.fetchall()
    except sqlite3.Error as e:
        print(e)
        exit(1)


def qry_all_transactions():
    ''' Query all transactions
    '''
    try:
        cur = CONN.cursor()
        cur.execute(
            sql_qry_all_transactions
        )
        return cur.fetchall()
    except sqlite3.Error as e:
        print(e)
        exit(1)


def qry_clerk(username):
    ''' Query a clerk
    '''
    try:
        cur = CONN.cursor()
        cur.execute(
            sql_qry_clerk, (username,)
        )
        return cur.fetchone()
    except sqlite3.Error as e:
        print(e)
        exit(1)


def qry_all_clerks():
    ''' Query all ckerks
    '''
    try:
        cur = CONN.cursor()
        cur.execute(
            sql_qry_all_clerks
        )
        return cur.fetchall()
    except sqlite3.Error as e:
        print(e)
        exit(1)


def upd_staff_password(username, password):
    ''' Update a staff's password
    '''
    try:
        cur = CONN.cursor()
        cur.execute(
            sql_upd_staff_password, (password, username)
        )
        CONN.commit()
        return cur.fetchone()
    except sqlite3.Error as e:
        print(e)
        exit(1)


def add_staff(username, password, is_manager):
    ''' Add a staff
    '''
    try:
        cur = CONN.cursor()
        cur.execute(
            sql_add_staff, (username, password, is_manager)
        )
        CONN.commit()
        return (username, password, is_manager)
    except sqlite3.Error as e:
        print(e)
        exit(1)


def del_staff(username):
    ''' Delete a staff
    '''
    try:
        cur = CONN.cursor()
        cur.execute(
            sql_del_staff, (username,)
        )
        CONN.commit()
    except sqlite3.Error as e:
        print(e)
        exit(1)


def add_item(item_name, item_descr, item_price):
    ''' Add an item
    '''
    try:
        cur = CONN.cursor()
        cur.execute(
            sql_add_item, (item_name, item_descr, item_price)
        )
        CONN.commit()
    except sqlite3.Error as e:
        print(e)
        exit(1)


def upd_item_descr(item_name, item_descr):
    ''' Update an item's description
    '''
    try:
        cur = CONN.cursor()
        cur.execute(
            sql_upd_item_descr, (item_descr, item_name)
        )
        CONN.commit()
    except sqlite3.Error as e:
        print(e)
        exit(1)


def upd_item_price(item_name, item_price):
    ''' Update an item's price
    '''
    try:
        cur = CONN.cursor()
        cur.execute(
            sql_upd_item_price, (item_price, item_name)
        )
        CONN.commit()
    except sqlite3.Error as e:
        print(e)
        exit(1)


def del_item(item_name):
    ''' Delete an item
    '''
    try:
        cur = CONN.cursor()
        cur.execute(
            sql_del_item, (item_name,)
        )
        CONN.commit()
    except sqlite3.Error as e:
        print(e)
        exit(1)
