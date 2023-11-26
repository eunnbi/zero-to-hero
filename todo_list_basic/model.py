class Todo:
    def __init__(self, id_: str, title: str, content: str, done=False):
        self.id = id_
        self.title = title
        self.content = content
        self.done = done

    def print_todo(self):
        print(f"ID: {self.id}")
        print(f"Title: {self.title}")
        print(f"Content: {self.content}")
        print(f"Done: {'Yes' if self.done else 'No'}")