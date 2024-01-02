from typing import Annotated, Generator

from fastapi import Depends

from database.engine import TODOS_TABLE_NAME, database


def _get_session() -> Generator:
    yield database


class Service:
    def __init__(self, session: Annotated[_get_session, Depends(_get_session)]):
        self.session = session
        self.todos_table_name = TODOS_TABLE_NAME
