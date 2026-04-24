from abc import ABC, abstractmethod

class ISellable(ABC):
    """Contrato para produtos de TI que podem ser comercializados."""
    @abstractmethod
    def sell(self, quantity: int):
        pass

class IDisplayable(ABC):
    """Contrato para exibir especificações técnicas detalhadas."""
    @abstractmethod
    def get_technical_sheet(self) -> str:
        pass
