from sqlalchemy.orm import Session

import models
import schemas


def get_todos(db: Session):
    return db.query(models.Todo).all()


def create_todo(db: Session, todo: schemas.TodoCreate):
    db_todo = models.Todo(title=todo.title, content=todo.content)
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return db_todo


def delete_todo(db: Session, todo_id: int):
    db_todo = db.query(models.Todo).filter(models.Todo.id == todo_id).first()
    if db_todo is None:
        return False
    else:
        db.delete(db_todo)
        db.commit()
        return True


def update_todo(db: Session, todo_id: int, todo: schemas.TodoUpdate):
    db_todo = db.query(models.Todo).filter(models.Todo.id == todo_id).first()
    if db_todo is not None:
        if todo.title is not None:
            db_todo.title = todo.title
        if todo.content is not None:
            db_todo.content = todo.content
        if todo.done is not None:
            db_todo.done = todo.done
        db.commit()
        db.refresh(db_todo)
    return db_todo
