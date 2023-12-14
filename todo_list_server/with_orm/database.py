from sqlmodel import create_engine
from models import SQLModel

DATABASE_URL = "sqlite:///sql_app.db"

engine = create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}, echo=True
)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)
