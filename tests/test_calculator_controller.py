import pytest
from app.models.models import CalculateRequest
from app.controllers.calculator_controller import CalculatorController


@pytest.mark.asyncio
async def test_calculator_controller():
    controller = CalculatorController()
    request = CalculateRequest(operation=["addition"], operands=[1, 2])
    response = await controller.calculate(request)
    assert response.result == 3
