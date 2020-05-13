import sqlite3


def create_entry_table():
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()

    cursor.execute('CREATE TABLE IF NOT EXISTS bills(customer_id integer primary key, customer_name text, bill_amt integer)')

    connection.commit()
    connection.close()


def get_all_entries():
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()

    cursor.execute('SELECT * FROM bills')
    entries = [{'customer_id': row[0], 'customer_name': row[1], 'bill_amt': row[2]} for row in cursor.fetchall()]

    connection.close()

    return entries


def add_entry(customer_id, customer_name, bill_amt):
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()

    try:
        cursor.execute('INSERT INTO bills VALUES(?, ?, ?)', (customer_id, customer_name, bill_amt))
    except sqlite3.IntegrityError:
        print("This customer id already exists in the database. Please enter another.")

    connection.commit()
    connection.close()


def show_entries():
    entries = get_all_entries()
    for entry in entries:
        print(f'Customer no. {entry["customer_id"]} {entry["customer_name"]} did a puurchase of {entry["bill_amt"]}.')


def find_entry(customer_name):
    entries = get_all_entries()
    for entry in entries:
        if entry["customer_name"] == customer_name:
            print(f'Customer no. {entry["customer_id"]} {entry["customer_name"]} did a puurchase of {entry["bill_amt"]}.')


def delete_entry(customer_id):
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()

    cursor.execute('DELETE FROM bills WHERE customer_id = ?', (customer_id, ))

    connection.commit()
    connection.close()
