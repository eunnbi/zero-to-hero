from fastapi import FastAPI, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from schemas import CommonResponseModel

app = FastAPI()


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(_: Request, exc: RequestValidationError):
    message = exc.errors()[0]["msg"]
    return JSONResponse(content={"error": message}, status_code=400)


@app.get('/add', response_model=CommonResponseModel)
async def get_addition_result(number1: float, number2: float):
    return JSONResponse(content={"data": {"result": number1 + number2}})


@app.get('/subtract', response_model=CommonResponseModel)
async def get_subtraction_result(number1: float, number2: float):
    return JSONResponse(content={"data": {"result": number1 - number2}})


@app.get('/multiply', response_model=CommonResponseModel)
async def get_multiplication_result(number1: float, number2: float):
    return JSONResponse(content={"data": {"result": number1 * number2}})


@app.get('/divide', response_model=CommonResponseModel)
async def get_division_result(number1: float, number2: float):
    if number2 == 0:
        return JSONResponse(content={"error": "The number cannot divide by zero"}, status_code=400)
    else:
        return JSONResponse(content={"data": {"result": number1 / number2}})
