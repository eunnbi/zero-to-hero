from databases import Database

DATABASE_URL = "sqlite:///sql_app.db"
TODOS_TABLE_NAME = "todos"

database = Database(DATABASE_URL)
