class Todo:
    id: int
    title: str
    content: str
    done: bool

    def __init__(self, row: (int, str, str, int)):
        self.id = row[0]
        self.title = row[1]
        self.content = row[2]
        self.done = row[3]

    def print_todo(self):
        print(f"ID: {self.id}")
        print(f"Title: {self.title}")
        print(f"Content: {self.content}")
        print(f"Done: {'Yes' if self.done else 'No'}")