from databases import Database

DATABASE_URL = "sqlite:///sql_app.db"
TODOS_TABLE_NAME = "todos"

database = Database(DATABASE_URL)


async def create_tables():
    query = f'''
        CREATE TABLE IF NOT EXISTS {TODOS_TABLE_NAME}(
            id INTEGER PRIMARY KEY AUTOINCREMENT, 
            title TEXT NOT NULL, 
            content TEXT NOT NULL, 
            done INTEGER DEFAULT 0
        )
        '''
    await database.execute(query)