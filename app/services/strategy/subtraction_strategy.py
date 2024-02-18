from .base_strategy import BaseStrategy


class SubtractionStrategy(BaseStrategy):
    def calculate(self, operands: list[float]) -> float:
        result = operands[0]
        for operand in operands[1:]:
            result -= operand
        return result
