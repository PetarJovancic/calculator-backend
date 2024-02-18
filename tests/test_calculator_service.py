import pytest
from app.services.calculator_service import CalculatorService


@pytest.fixture
def service():
    return CalculatorService()


def test_service_execute_addition(service):
    result = service.execute("addition", [3, 3])
    assert result == 6


def test_service_execute_percentage(service):
    result = service.execute("percentage", [50])
    assert result == 0.5


def test_service_execute_unsupported_operation(service):
    with pytest.raises(ValueError):
        service.execute("unsupported", [1, 2])
