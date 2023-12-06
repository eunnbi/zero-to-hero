from typing import Generic, TypeVar
from pydantic import BaseModel

DataT = TypeVar('DataT')


class SuccessResponse(BaseModel, Generic[DataT]):
    data: DataT


class TodoBase(BaseModel):
    title: str
    content: str


class TodoCreate(TodoBase):
    pass


class Todo(TodoBase):
    id: int
    done: bool


class TodoUpdate(BaseModel):
    title: str | None = None
    content: str | None = None
    done: bool | None = None
