from pydantic import BaseModel


class _TodoBase(BaseModel):
    title: str
    content: str


class TodoCreate(_TodoBase):
    pass


class Todo(_TodoBase):
    id: int
    done: bool


class TodoUpdate(BaseModel):
    title: str | None = None
    content: str | None = None
    done: bool | None = None
