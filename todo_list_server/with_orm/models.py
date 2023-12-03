from typing import Optional

from sqlmodel import Field, SQLModel


class TodoBase(SQLModel):
    title: str
    content: str


class Todo(TodoBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    done: Optional[bool] = Field(default=False)


class TodoCreate(TodoBase):
    pass


class TodoUpdate(SQLModel):
    title: Optional[str] = None
    content: Optional[str] = None
    done: Optional[bool] = None
