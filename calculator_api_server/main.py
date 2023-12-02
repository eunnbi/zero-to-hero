from fastapi import FastAPI, Request, HTTPException
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

from schemas import SuccessResponseModel, CalculationResult

app = FastAPI()


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(_: Request, exc: RequestValidationError):
    message = exc.errors()[0]["msg"]
    return JSONResponse(content={"detail": message}, status_code=400)


@app.get(path='/add', response_model=SuccessResponseModel[CalculationResult])
async def get_addition_result(number1: float, number2: float):
    return SuccessResponseModel(data=CalculationResult(result=number1 + number2))


@app.get(path='/subtract', response_model=SuccessResponseModel[CalculationResult])
async def get_subtraction_result(number1: float, number2: float):
    return SuccessResponseModel(data=CalculationResult(result=number1 - number2))


@app.get(path='/multiply', response_model=SuccessResponseModel[CalculationResult])
async def get_multiplication_result(number1: float, number2: float):
    return SuccessResponseModel(data=CalculationResult(result=number1 * number2))


@app.get(path='/divide', response_model=SuccessResponseModel[CalculationResult])
async def get_division_result(number1: float, number2: float):
    if number2 == 0:
        raise HTTPException(status_code=400, detail="The number cannot divide by zero")
    else:
        return SuccessResponseModel(data=CalculationResult(result=number1 / number2))
