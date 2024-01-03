from app.service import Service
from database.models import Todo


class TodosService(Service):
    async def get_todos(self):
        query = f"SELECT id, title, content, done from {self.todos_table_name}"
        data = await self.session.fetch_all(query)
        return [{**i} for i in data]

    async def get_todo(self, todo_id: int):
        query = f"SELECT id, title, content, done from {self.todos_table_name} WHERE id={todo_id}"
        data = await self.session.fetch_one(query)
        return data

    async def create_todo(self, title: str, content: str):
        query = f"INSERT INTO {self.todos_table_name} (title, content) VALUES (:title, :content)"
        values = { "title": title, "content": content }
        id = await self.session.execute(query=query, values=values)
        return await self.get_todo(id)

    async def update_todo(self, todo_id: int, title: str | None, content: str | None, done: bool | None):
        db_todo = await self.get_todo(todo_id)
        if db_todo is not None:
            query = f"UPDATE {self.todos_table_name} SET title=:title, content=:content, done=:done WHERE id=:id"
            todo_data = {"id": todo_id, "title": title, "content": content, "done": done}
            new_todo = Todo(id=todo_id, title=db_todo.title, content=db_todo.content, done=db_todo.done)
            for key, value in todo_data.items():
                if value is not None:
                    setattr(new_todo, key, value)
            await self.session.execute(query=query, values=new_todo.__dict__)
            return await self.get_todo(todo_id)
        else:
            return db_todo

    async def delete_todo(self, todo_id: int):
        db_todo = await self.get_todo(todo_id)
        if db_todo is not None:
            query = f"DELETE FROM {self.todos_table_name} WHERE id=:id"
            values = {"id": todo_id}
            await self.session.execute(query=query, values=values)
            return True
        else:
            return False
