import sqlite3
from typing import List
import datetime
from model import Todo

db_connection = sqlite3.connect('todos.db')
c = db_connection.cursor()

def create_table():
    c.execute("""CREATE TABLE IF NOT EXISTS todos(
              task text,
              category text,
              created_at text,
              completed_at text,
              status integer,
              id integer
              )""")

create_table()

def insert_todo(todo: Todo):
    c.execute('select count(*) FROM todos')
    count = c.fetchone()[0]
    todo.id = count if count else 0
    with db_connection:
        c.execute('INSERT INTO todos VALUES (:task, :category, :created_at, :completed_at, :status, :id)',
                  {'task': todo.task, 'category': todo.category, 'created_at': todo.created_at, 'completed_at': todo.completed_at, 'status': todo.status, 'id': todo.id}
                )
        
def get_all_todos():
    c.execute('select * from todos')
    results = c.fetchall()
    todos = []
    for todo in results:
        todos.append(Todo(*todo))
    return todos

def delete_todo(id):
    c.execute('select count(*) from todos')
    count = c.fetchone[0]

    with db_connection:
        c.execute("DELETE from todos WHERE id=:id", {'id': id})
        for id in range(id+1, count):
            change_id(id, id-1, False)

def change_id(old_id: int, new_id: int, commit=True):
    c.execute("UPDATE todos SET id=:id_new WHERE id=:id_old", {'id_old': old_id, 'id_new': new_id})
    if commit:
        db_connection.commit()

def update_todo(id: int, task: str, category: str):
    with db_connection:
        if task is not None and category is not None:
            c.execute('UPDATE todos SET task=:task, category=:category WHERE id=:id', {'id': id, 'task': task, 'category': category})
        elif task is not None:
            c.execute('UPDATE todos SET task=:task WHERE id=:id', {'id': id, 'task': task})
        elif category is not None:
            c.execute('UPDATE todos SET category=:category WHERE id=:id', {'id': id, 'category': category})

def complete_todo(id: int):
    with db_connection:
        c.execute('UPDATE todos SET status = 2, completed_at = :completed_at WHERE id = :id',
                  {'id': id, 'completed_at': datetime.datetime.now().isoformat()})