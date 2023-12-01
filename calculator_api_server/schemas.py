from typing import TypeVar, Generic

from pydantic import BaseModel


class CalculationResult(BaseModel):
    result: float


DataT = TypeVar('DataT')


class SuccessResponseModel(BaseModel, Generic[DataT]):
    data: DataT


