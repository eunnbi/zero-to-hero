from typing import Generic, TypeVar
from pydantic.generics import GenericModel

from sqlmodel import Field, SQLModel


class TodoBase(SQLModel):
    title: str
    content: str


class Todo(TodoBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    done: bool | None = False


class TodoCreate(TodoBase):
    pass


class TodoRead(TodoBase):
    id: int
    done: bool


class TodoUpdate(SQLModel):
    title: bool | None = None
    content: bool | None = None
    done: bool | None = None


SQLSchema = TypeVar("SQLSchema")


class SuccessResponse(GenericModel, Generic[SQLSchema]):
    data: SQLSchema
