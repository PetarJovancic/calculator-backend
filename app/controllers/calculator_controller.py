from ..models.models import CalculateRequest, CalculateResponse, ResultFormat
from ..services.calculator_service import CalculatorService
from fastapi import HTTPException


class CalculatorController:
    def __init__(self):
        self.calculator_service = CalculatorService()

    async def calculate(self, request: CalculateRequest) -> CalculateResponse:
        if len(request.operation) == 0 or len(request.operands) == 0:
            raise HTTPException(status_code=400, detail=str("Bad Request."))
        elif len(request.operation) > 1 or len(request.operands) > 2:
            # Placehodler to call complex operation when implementation is done
            raise HTTPException(
                            status_code=501,
                            detail=str("Complex Operations Not Implemented."))
        else:
            result = self.calculator_service.execute(
                                        request.operation[0], request.operands)

        if isinstance(result, float):
            color = "red" if result % 2 else "green"
        else:
            color = "red"

        return CalculateResponse(result=result,
                                 format=ResultFormat(color=color))
