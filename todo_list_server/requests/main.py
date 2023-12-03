import requests
import json

BASE_URL = "http://localhost:8000"


class Todo:
    def __init__(self, title: str, content: str):
        self.title = title
        self.content = content


def add_todos():
    headers = {"Content-Type": "application/json"}
    for i in range(1000):
        body = Todo(title=f"test ${i}", content=f"add todo test {i}")
        try:
            response = requests.post(url=f"{BASE_URL}/todos", headers=headers, data=json.dumps(body.__dict__))
            data = response.json()
            print(f"success: {data}")
        except Exception as ex:
            print(f"error: {ex}")


if __name__ == '__main__':
    add_todos()
