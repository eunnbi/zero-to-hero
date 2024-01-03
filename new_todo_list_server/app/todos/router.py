from typing import Annotated

from fastapi import APIRouter, HTTPException, Depends
from starlette.responses import Response

from app.schemas import SuccessResponse
from app.todos.schemas import Todo, TodoCreate, TodoUpdate
from app.todos.service import TodosService

todos_router = APIRouter(prefix="/todos")

ServiceDep = Annotated[TodosService, Depends(TodosService)]


@todos_router.get(path='/')
async def read_todos(service: ServiceDep) -> SuccessResponse[list[Todo]]:
    todos = await service.get_todos()
    return SuccessResponse(data=todos)


@todos_router.post(path='/')
async def create_todo(todo: TodoCreate, service: ServiceDep) -> SuccessResponse[Todo]:
    new_todo = await service.create_todo(title=todo.title, content=todo.content)
    return SuccessResponse(data=new_todo)


@todos_router.patch(path='/{todo_id}')
async def update_todo(todo_id: int, todo: TodoUpdate, service: ServiceDep) -> SuccessResponse[Todo]:
    new_todo = await service.update_todo(todo_id=todo_id, title=todo.title, content=todo.content, done=todo.done)
    if new_todo is None:
        raise HTTPException(status_code=404, detail="Item not found")
    else:
        return SuccessResponse(data=new_todo)


@todos_router.delete(path='/{todo_id}')
async def delete_todo(todo_id: int, service: ServiceDep):
    exist = await service.delete_todo(todo_id=todo_id)
    if not exist:
        raise HTTPException(status_code=404, detail="Item not found")
    else:
        return Response()
