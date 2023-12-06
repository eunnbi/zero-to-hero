from sqlmodel import Session, select

import models


def get_todos(db: Session):
    return db.exec(select(models.Todo)).all()


def get_todo(db: Session, todo_id: int):
    return db.get(models.Todo, todo_id)


def create_todo(db: Session, todo: models.TodoCreate):
    db_todo = models.Todo.from_orm(todo)
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return db_todo


def update_todo(db: Session, todo_id: int, todo: models.TodoUpdate):
    db_todo = get_todo(db, todo_id)
    if db_todo is not None:
        todo_data = todo.dict(exclude_unset=True, exclude_none=True)
        for key, value in todo_data.items():
            setattr(db_todo, key, value)
        db.add(db_todo)
        db.commit()
        db.refresh(db_todo)
    return db_todo


def delete_todo(db: Session, todo_id: int):
    db_todo = get_todo(db, todo_id)
    if db_todo is not None:
        db.delete(db_todo)
        db.commit()
        return True
    else:
        return False
