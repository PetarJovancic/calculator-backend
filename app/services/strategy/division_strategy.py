from .base_strategy import BaseStrategy


class DivisionStrategy(BaseStrategy):
    def calculate(self, operands: list[float]) -> float:
        if len(operands) < 2:
            raise ValueError("Division requires at least two operands.")

        result = operands[0]
        for operand in operands[1:]:
            if operand == 0:
                return "Error"
            result /= operand

        return result
