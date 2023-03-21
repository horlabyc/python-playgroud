import sqlite3

db_connection = sqlite3.connect('stocks.db')
cursor = db_connection.cursor()

def create_table():
    cursor.execute("""CREATE TABLE IF NOT EXISTS stocks(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name    text,
        category    text,
        created_at  text,
        updated_at  text,
        quantity    integer
        )""")

create_table()