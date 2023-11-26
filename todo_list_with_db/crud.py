import sqlite3
from database import TODO_LIST_TABLE
from model import Todo


def get_todo_list(conn: sqlite3.Connection):
    cursor = conn.cursor()
    cursor.execute(f"SELECT id, title, content, done FROM {TODO_LIST_TABLE}")
    data = cursor.fetchall()
    cursor.close()
    todo_list = [Todo(row) for row in data]
    return todo_list


def add_todo(conn: sqlite3.Connection, title: str, content: str):
    cursor = conn.cursor()
    cursor.execute(f"INSERT INTO {TODO_LIST_TABLE} (title, content) VALUES (?,?)", (title, content))
    cursor.close()
    conn.commit()


def delete_todo(conn: sqlite3.Connection, todo_id: int):
    cursor = conn.cursor()
    cursor.execute(f"DELETE FROM {TODO_LIST_TABLE} WHERE id=?", (todo_id,))
    cursor.close()
    conn.commit()


def toggle_todo_done(conn: sqlite3.Connection, todo_id: int):
    cursor = conn.cursor()
    cursor.execute(f"SELECT id, done FROM {TODO_LIST_TABLE} WHERE id=?", (todo_id,))
    data = cursor.fetchone()
    if data is not None:
        todo = Todo(data)
        cursor.execute(f"UPDATE {TODO_LIST_TABLE} SET done=? WHERE id=?", (not todo.done, todo.id))
    cursor.close()
    conn.commit()