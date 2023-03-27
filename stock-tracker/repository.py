import sqlite3
from model import Inventory

db_connection = sqlite3.connect('inventories.db')
cursor = db_connection.cursor()

def create_table():
    cursor.execute("""CREATE TABLE IF NOT EXISTS inventories(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name    text,
        category    text,
        quantity    integer,
        created_at  text,
        updated_at  text
        )""")

create_table()

def get_all_stocks():
    cursor.execute('select * from inventories')
    all_stocks = cursor.fetchall()
    stocks = []
    for stock in all_stocks:
        stocks.append(Inventory(stock[1], stock[2], stock[3], stock[4], stock[5], stock[0]))
    return stocks

def insert_stock(stock: Inventory):
    cursor.execute("SELECT * FROM inventories WHERE LOWER(name) = ?", (stock.name.lower(),))
    results = cursor.fetchall()
    if len(results):
        existing_stock = results[0]
        print(existing_stock)
        new_quantity = existing_stock[3] + stock.quantity
        id = existing_stock[0]
        with db_connection:
            cursor.execute("UPDATE inventories SET quantity=:quantity WHERE id=:id", {'id': id, 'quantity': new_quantity})
    else:
        with db_connection:
            cursor.execute(
                'INSERT INTO inventories(name, category, created_at, updated_at, quantity) VALUES(?,?,?,?,?)', 
                (stock.name, stock.category, stock.created_at, stock.updated_at, stock.quantity)
            )

def reduce_stock_quantity(id: int, quantity: str):
    cursor.execute("SELECT * FROM inventories WHERE id=:id", {'id': id})
    stock = cursor.fetchone()
    if not stock:
        print("Stock not valid")
        return
    else:
        new_stock_quantity = stock[3] - quantity
        if new_stock_quantity < 0:
            print('Insufficient stock')
            return
        else:
            with db_connection:
                cursor.execute("UPDATE inventories SET quantity=:quantity WHERE id=:id", {'id': id, 'quantity': new_stock_quantity})

def increase_stock_quantity(id: int, quantity: str):
    cursor.execute("SELECT * FROM inventories WHERE id=:id", {'id': id})
    stock = cursor.fetchone()
    if not stock:
        print("Stock not valid")
        return
    else:
        new_stock_quantity = stock[3] + quantity
        with db_connection:
                cursor.execute("UPDATE inventories SET quantity=:quantity WHERE id=:id", {'id': id, 'quantity': new_stock_quantity})

def delete_stock(id):
    with db_connection:
        cursor.execute("DELETE from inventories WHERE id=:id", {'id': id})
