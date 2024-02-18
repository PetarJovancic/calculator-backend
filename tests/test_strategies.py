import pytest
from app.services.strategy.addition_strategy import AdditionStrategy
from app.services.strategy.percentage_strategy import PercentageStrategy
from app.services.strategy.division_strategy import DivisionStrategy
from app.services.strategy.multiplication_strategy import (
    MultiplicationStrategy,
)
from app.services.strategy.subtraction_strategy import SubtractionStrategy


def test_addition_strategy():
    strategy = AdditionStrategy()
    result = strategy.calculate([1, 2])
    assert result == 3


def test_percentage_strategy():
    strategy = PercentageStrategy()
    result = strategy.calculate([50])
    assert result == 0.5


def test_division_normal():
    strategy = DivisionStrategy()
    assert strategy.calculate([10, 2]) == 5


def test_division_by_zero():
    strategy = DivisionStrategy()
    assert strategy.calculate([10, 0]) == "Error"


def test_division_insufficient_operands():
    strategy = DivisionStrategy()
    with pytest.raises(ValueError):
        strategy.calculate([10])


def test_multiplication_normal():
    strategy = MultiplicationStrategy()
    assert strategy.calculate([2, 3]) == 6


def test_multiplication_by_zero():
    strategy = MultiplicationStrategy()
    assert strategy.calculate([0, 3]) == 0


def test_multiplication_no_operands():
    strategy = MultiplicationStrategy()
    assert strategy.calculate([]) == 1


def test_subtraction_normal():
    strategy = SubtractionStrategy()
    assert strategy.calculate([10, 3]) == 7


def test_subtraction_result_negative():
    strategy = SubtractionStrategy()
    assert strategy.calculate([10, 15]) == -5


def test_subtraction_single_operand():
    strategy = SubtractionStrategy()
    assert strategy.calculate([10]) == 10
