#!/usr/bin/env python3


sql_tables = (
    (
        'members',
        '''
        CREATE TABLE IF NOT EXISTS members (
            card_no integer PRIMARY KEY,
            password text NOT NULL,
            name text NOT NULL,
            gender text NOT NULL,
            phone text NOT NULL UNIQUE,
            email text,
            address text NOT NULL,
            balance integer NOT NULL
        );
        ''',
    ),
    (
        'staffs',
        '''
        CREATE TABLE IF NOT EXISTS staffs (
            username text PRIMARY KEY,
            password text NOT NULL,
            is_manager integer NOT NULL
        );
        ''',
    ),
    (
        'items',
        '''
        CREATE TABLE IF NOT EXISTS items (
            name text PRIMARY KEY ,
            descr text NOT NULL,
            price integer NOT NULL
        );
        ''',
    ),
    (
        'transactions',
        '''
        CREATE TABLE IF NOT EXISTS transactions (
            id integer PRIMARY KEY,
            card_no text NOT NULL,
            item_name integer NOT NULL,
            item_price integer NOT NULL,
            date integer NOT NULL,
            FOREIGN KEY(card_no) REFERENCES member(card_no)
        );
        ''',
    )
)
