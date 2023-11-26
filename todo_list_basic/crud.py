from model import Todo
import uuid


def add_todo(todo_list: dict[str, Todo], title: str, content: str):
    id = str(uuid.uuid4())
    todo_item = Todo(id_=id, title=title, content=content)
    todo_list[id] = todo_item


def delete_todo(todo_list: dict[str, Todo], todo_id: str):
    try:
        del todo_list[todo_id]
    except KeyError:
        print(f"Error: There's no todo with ID {todo_id}")


def toggle_todo_done(todo_list: dict[str, Todo], todo_id: str):
    try:
        todo = todo_list[todo_id]
        todo.done = not todo.done
    except KeyError:
        print(f"Error: There's no todo with ID {todo_id}")
