from abc import ABC, abstractmethod


class BaseStrategy(ABC):
    @abstractmethod
    def calculate(self, operands: list[float]) -> float:
        pass
