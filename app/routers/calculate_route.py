from fastapi import Body, HTTPException, Depends, APIRouter
from ..models.models import CalculateRequest, CalculateResponse
from ..controllers.calculator_controller import CalculatorController


router = APIRouter()


@router.post("/calculate", response_model=CalculateResponse)
async def calculate(request: CalculateRequest = Body(...),
                    controller: CalculatorController = Depends(
                                                        CalculatorController)):
    try:
        return await controller.calculate(request)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
