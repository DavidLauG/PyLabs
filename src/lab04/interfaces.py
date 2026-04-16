from abc import ABC, abstractmethod

class ISellable(ABC):
    """Contrato para objetos que podem ser vendidos."""
    @abstractmethod
    def sell(self, quantity: int):
        pass

class IDisplayable(ABC):
    """Contrato para objetos que podem ser exibidos de forma formatada."""
    @abstractmethod
    def get_info_formatted(self) -> str:
        pass
