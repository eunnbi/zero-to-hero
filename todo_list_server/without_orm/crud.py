import schemas
from database import database, TODOS_TABLE_NAME


async def get_todos():
    query = f"SELECT id, title, content, done from {TODOS_TABLE_NAME}"
    data = await database.fetch_all(query)
    return [{**i} for i in data]


async def get_todo(todo_id: int):
    query = f"SELECT id, title, content, done from {TODOS_TABLE_NAME} WHERE id={todo_id}"
    data = await database.fetch_one(query)
    return data


async def create_todo(todo: schemas.TodoCreate):
    query = f"INSERT INTO {TODOS_TABLE_NAME} (title, content) VALUES (:title, :content)"
    id = await database.execute(query=query, values=todo.__dict__)
    return await get_todo(id)


async def update_todo(todo_id: int, todo: schemas.TodoUpdate):
    db_todo = await get_todo(todo_id)
    if db_todo is not None:
        query = f"UPDATE {TODOS_TABLE_NAME} SET title=:title, content=:content, done=:done WHERE id=:id"
        new_todo = schemas.Todo(
            id=todo_id,
            title=db_todo.title if todo.title is None else todo.title,
            content=db_todo.content if todo.content is None else todo.content,
            done=db_todo.done if todo.done is None else todo.done
        )
        await database.execute(query=query, values=new_todo.__dict__)
        return await get_todo(todo_id)
    else:
        return db_todo


async def delete_todo(todo_id: int):
    db_todo = await get_todo(todo_id)
    if db_todo is not None:
        query = f"DELETE FROM {TODOS_TABLE_NAME} WHERE id=:id"
        values = {"id": todo_id}
        await database.execute(query=query, values=values)
        return True
    else:
        return False
