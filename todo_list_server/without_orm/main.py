from fastapi import FastAPI, HTTPException, Response, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

import crud
import schemas
from database import database, create_tables

app = FastAPI()


@app.on_event("startup")
async def on_startup():
    await database.connect()
    await create_tables()


@app.on_event("shutdown")
async def on_shutdown():
    await database.disconnect()


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(_: Request, exc: RequestValidationError):
    message = exc.errors()[0]["msg"]
    return JSONResponse(content={"detail": message}, status_code=400)


@app.get(path='/todos', response_model=schemas.SuccessResponse[list[schemas.Todo]])
async def read_todos():
    todos = await crud.get_todos()
    return schemas.SuccessResponse(data=todos)


@app.post(path='/todos', response_model=schemas.SuccessResponse[schemas.Todo])
async def create_todo(todo: schemas.TodoCreate):
    new_todo = await crud.create_todo(todo=todo)
    return schemas.SuccessResponse(data=new_todo)


@app.patch(path='/todos/{todo_id}', response_model=schemas.SuccessResponse[schemas.Todo])
async def update_todo(todo_id: int, todo: schemas.TodoUpdate):
    new_todo = await crud.update_todo(todo_id=todo_id, todo=todo)
    if new_todo is None:
        raise HTTPException(status_code=404, detail="Item not found")
    else:
        return schemas.SuccessResponse(data=new_todo)


@app.delete(path='/todos/{todo_id}')
async def delete_todo(todo_id: int):
    exist = await crud.delete_todo(todo_id=todo_id)
    if not exist:
        raise HTTPException(status_code=404, detail="Item not found")
    else:
        return Response()
