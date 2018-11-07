#!/usr/bin/env python3


# ------------ staffs ------------

sql_add_staff = '''
    INSERT INTO staffs(username, password, is_manager)
    VALUES(?,?,?)
'''

sql_qry_staff = '''
    SELECT * FROM staffs WHERE username=?
'''

sql_qry_clerk = '''
    SELECT * FROM staffs WHERE username=? AND is_manager=0
'''

sql_qry_all_clerks = '''
    SELECT * FROM staffs WHERE is_manager=0
'''

sql_upd_staff_password = '''
    UPDATE staffs SET password=? WHERE username=?
'''

sql_del_staff = '''
    DELETE FROM staffs WHERE username=?
'''

# ------------ members ------------

sql_add_member = '''
    INSERT INTO members(card_no, password, name, gender, phone, email, address, balance)
    VALUES(?,?,?,?,?,?,?,?)
'''

sql_qry_member = '''
    SELECT * FROM members WHERE card_no=?
'''

sql_qry_member_by_phone = '''
    SELECT * FROM members WHERE phone=?
'''

sql_qry_member_last = '''
    SELECT * FROM members ORDER BY card_no DESC LIMIT 1
'''

sql_upd_member_balance = '''
    UPDATE members SET balance=? WHERE card_no=?
'''

sql_del_member = '''
    DELETE FROM members WHERE card_no=?
'''

sql_qry_all_members = '''
    SELECT * FROM members
'''

# ------------ items ------------

sql_qry_item = '''
    SELECT * FROM items WHERE name=?
'''

sql_qry_all_items = '''
    SELECT * FROM items
'''

sql_add_item = '''
    INSERT INTO items(name, descr, price)
    VALUES(?,?,?)
'''

sql_upd_item_descr = '''
    UPDATE items SET descr=? WHERE name=?
'''

sql_upd_item_price = '''
    UPDATE items SET price=? WHERE name=?
'''

sql_del_item = '''
    DELETE FROM items WHERE name=?
'''

# ------------ transactions ------------

sql_add_transaction = '''
    INSERT INTO transactions(card_no, item_name, item_price, date)
    VALUES(?,?,?,?)
'''

sql_qry_transactions_by_card_no = '''
    SELECT * FROM transactions WHERE card_no=?
'''

sql_qry_transactions_by_item_name = '''
    SELECT * FROM transactions WHERE item_name=?
'''

sql_qry_transactions_by_date = '''
    SELECT * FROM transactions WHERE date=?
'''

sql_qry_all_transactions = '''
    SELECT * FROM transactions
'''
