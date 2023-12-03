from fastapi import FastAPI, Depends, Response, Request, HTTPException
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

from sqlalchemy.orm import Session

from database import SessionLocal, engine
from models import Base

import crud
import schemas

Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


app = FastAPI()


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(_: Request, exc: RequestValidationError):
    message = exc.errors()[0]["msg"]
    return JSONResponse(content={"detail": message}, status_code=400)


@app.get(path='/todos', response_model=schemas.SuccessResponse[list[schemas.Todo]])
async def read_todos(db: Session = Depends(get_db)):
    todos = crud.get_todos(db)
    return schemas.SuccessResponse(data=todos)


@app.post(path='/todos', response_model=schemas.SuccessResponse[schemas.Todo])
async def create_todo(todo: schemas.TodoCreate, db: Session = Depends(get_db)):
    new_todo = crud.create_todo(db=db, todo=todo)
    return schemas.SuccessResponse(data=new_todo)


@app.patch(path='/todos/{todo_id}', response_model=schemas.SuccessResponse[schemas.Todo])
async def update_todo(todo_id: int, todo: schemas.TodoUpdate, db: Session = Depends(get_db)):
    new_todo = crud.update_todo(db=db, todo_id=todo_id, todo=todo)
    if new_todo is None:
        raise HTTPException(status_code=400, detail="Item not found")
    else:
        return schemas.SuccessResponse(data=new_todo)


@app.delete(path='/todos/{todo_id}')
async def delete_todo(todo_id: int, db: Session = Depends(get_db)):
    exist = crud.delete_todo(db=db, todo_id=todo_id)
    if not exist:
        raise HTTPException(status_code=400, detail="Item not found")
    else:
        return Response()
