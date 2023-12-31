from fastapi import FastAPI, Response, Request, HTTPException
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from sqlmodel import Session

from database import create_db_and_tables, engine

import crud
import models

app = FastAPI()


@app.on_event("startup")
def on_startup():
    create_db_and_tables()


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(_: Request, exc: RequestValidationError):
    message = exc.errors()[0]["msg"]
    return JSONResponse(content={"detail": message}, status_code=400)


@app.get(path='/todos')
async def read_todos() -> models.SuccessResponse[list[models.TodoRead]]:
    with Session(engine) as session:
        todos = crud.get_todos(session)
        return models.SuccessResponse(data=todos)


@app.post(path='/todos')
async def create_todo(todo: models.TodoCreate) -> models.SuccessResponse[models.TodoRead]:
    with Session(engine) as session:
        new_todo = crud.create_todo(db=session, todo=todo)
        return models.SuccessResponse(data=new_todo)


@app.patch(path='/todos/{todo_id}')
async def update_todo(todo_id: int, todo: models.TodoUpdate) -> models.SuccessResponse[models.TodoRead]:
    with Session(engine) as session:
        new_todo = crud.update_todo(db=session, todo_id=todo_id, todo=todo)
        if new_todo is None:
            raise HTTPException(status_code=404, detail="Item not found")
        else:
            return models.SuccessResponse(data=new_todo)


@app.delete(path='/todos/{todo_id}')
async def delete_todo(todo_id: int):
    with Session(engine) as session:
        exist = crud.delete_todo(db=session, todo_id=todo_id)
        if not exist:
            raise HTTPException(status_code=404, detail="Item not found")
        else:
            return Response()
