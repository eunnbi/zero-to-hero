from typing import Optional, Generic, TypeVar
from pydantic.generics import GenericModel

from sqlmodel import Field, SQLModel


class TodoBase(SQLModel):
    title: str
    content: str


class Todo(TodoBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    done: Optional[bool] = Field(default=False)


class TodoCreate(TodoBase):
    pass


class TodoRead(TodoBase):
    id: int
    done: bool


class TodoUpdate(SQLModel):
    title: Optional[str] = None
    content: Optional[str] = None
    done: Optional[bool] = None


SQLSchema = TypeVar("SQLSchema")


class SuccessResponse(GenericModel, Generic[SQLSchema]):
    data: SQLSchema
