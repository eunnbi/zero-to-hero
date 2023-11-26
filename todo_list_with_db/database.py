import sqlite3

TODO_LIST_TABLE = "TODO_LIST"


def get_db_connection():
    conn = sqlite3.connect("todo-list.db")
    return conn


def create_todo_list_table(conn: sqlite3.Connection):
    cursor = conn.cursor()
    query = f'''
        CREATE TABLE IF NOT EXISTS {TODO_LIST_TABLE}(
            id INTEGER PRIMARY KEY AUTOINCREMENT, 
            title TEXT NOT NULL, 
            content TEXT NOT NULL, 
            done INTEGER DEFAULT 0
        )
        '''
    cursor.execute(query)
    cursor.close()