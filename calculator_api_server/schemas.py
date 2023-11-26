from pydantic import BaseModel


class CalculationResult(BaseModel):
    result: float


class CommonResponseModel(BaseModel):
    data: CalculationResult
