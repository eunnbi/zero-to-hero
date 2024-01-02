from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from starlette.requests import Request

from database.engine import database, create_tables

from app.todos.router import todos_router

app = FastAPI()


@app.on_event('startup')
async def on_startup():
    await database.connect()
    await create_tables()


@app.on_event('shutdown')
async def on_shutdown():
    await database.disconnect()


@app.exception_handler(RequestValidationError)
def handle_request_validation_exception(_: Request, exc: RequestValidationError):
    message = exc.errors()[0]["msg"]
    return JSONResponse(content={"detail": message}, status_code=400)


@app.exception_handler(HTTPException)
def handle_http_exception(_: Request, exc: HTTPException) -> JSONResponse:
    return JSONResponse(
        content={"detail": exc.detail},
        status_code=exc.status_code,
        headers={"Content-Type": "application/json"},
    )


app.include_router(todos_router)
