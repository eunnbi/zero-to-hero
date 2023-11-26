import json
import os
from model import Todo

FILE_NAME = 'todo-list.json'


def create_todo_list_file():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w") as file:
            file.write('[]')


def get_saved_todo_list() -> dict[str, Todo]:
    create_todo_list_file()
    with open(FILE_NAME, 'r', encoding='utf-8') as f:
        try:
            data = json.load(f)
            todo_list: dict[str, Todo] = {
                item['id']: Todo(id_=item["id"], title=item["title"], content=item["content"], done=item["done"])
                for item in data
            }
            return todo_list
        except json.JSONDecodeError:
            print("Error: The json file has invalid syntax")
            return {}
        except KeyError:
            print("Error: The json file has invalid field name")
            return {}


def save_todo_list(todo_list: dict[str, Todo]):
    saved_todo_list = [todo.__dict__ for todo in todo_list.values()]
    with open(FILE_NAME, 'w') as f:
        json.dump(saved_todo_list, f, indent=2)
