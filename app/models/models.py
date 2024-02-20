from pydantic import BaseModel, Field
from typing import List, Optional, Union


class CalculateRequest(BaseModel):
    operation: List[str] = Field(..., example=["addition"])
    operands: List[float] = Field(..., example=[1, 2])


class ResultFormat(BaseModel):
    color: Optional[str] = None


class CalculateResponse(BaseModel):
    result: Union[float, str]
    format: Optional[ResultFormat] = None
