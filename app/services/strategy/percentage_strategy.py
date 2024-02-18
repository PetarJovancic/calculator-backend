from .base_strategy import BaseStrategy


class PercentageStrategy(BaseStrategy):
    def calculate(self, operands: list[float]) -> float:
        if len(operands) != 1:
            raise ValueError(
                    "Percentage calculation requires exactly one operands.")
        return (operands[0] / 100)
