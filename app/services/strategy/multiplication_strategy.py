from .base_strategy import BaseStrategy


class MultiplicationStrategy(BaseStrategy):
    def calculate(self, operands: list[float]) -> float:
        result = 1
        for operand in operands:
            result *= operand
        return result
