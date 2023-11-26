from model import Todo
from file_io import save_todo_list, get_saved_todo_list
import uuid


def get_todo_list():
    return get_saved_todo_list()


def add_todo(todo_list: dict[str, Todo], title: str, content: str):
    id = str(uuid.uuid4())
    todo_item = Todo(id_=id, title=title, content=content)
    todo_list[id] = todo_item
    save_todo_list(todo_list)


def delete_todo(todo_list: dict[str, Todo], todo_id: str):
    try:
        del todo_list[todo_id]
        save_todo_list(todo_list)
    except KeyError:
        print(f"Error: There's no todo with ID {todo_id}")


def toggle_todo_done(todo_list: dict[str, Todo], todo_id: str):
    try:
        todo = todo_list[todo_id]
        todo.done = not todo.done
        save_todo_list(todo_list)
    except KeyError:
        print(f"Error: There's no todo with ID {todo_id}")
