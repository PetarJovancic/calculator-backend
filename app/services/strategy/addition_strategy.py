from .base_strategy import BaseStrategy


class AdditionStrategy(BaseStrategy):
    def calculate(self, operands: list[float]) -> float:
        return sum(operands)
