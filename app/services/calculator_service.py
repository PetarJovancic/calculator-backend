from .strategy.addition_strategy import AdditionStrategy
from .strategy.division_strategy import DivisionStrategy
from .strategy.subtraction_strategy import SubtractionStrategy
from .strategy.multiplication_strategy import MultiplicationStrategy
from .strategy.percentage_strategy import PercentageStrategy


class CalculatorService:
    def __init__(self):
        self.strategies = {
            "addition": AdditionStrategy(),
            "division": DivisionStrategy(),
            "subtraction": SubtractionStrategy(),
            "multiplication": MultiplicationStrategy(),
            "percentage": PercentageStrategy(),
            # Placeholder for future strategies
        }

    def execute(self, operation, operands):
        strategy = self.strategies.get(operation)
        if strategy:
            return strategy.calculate(operands)
        else:
            raise ValueError("Unsupported operation")
