from typing import TypeVar, Generic, Callable, Optional, List, Protocol, Any

# --- PROTOCOLOS (Nota 5 - Tipagem Estrutural) ---
class Displayable(Protocol):
    """Protocolo para objetos que podem ser exibidos."""
    def display(self) -> str:
        ...

class Scorable(Protocol):
    """Protocolo para objetos que possuem uma pontuação/valor numérico."""
    def score(self) -> float:
        ...

# --- TYPEVARS ---
T = TypeVar('T') # Tipo Genérico irrestrito
R = TypeVar('R') # Tipo de Retorno para o Map
D = TypeVar('D', bound=Displayable) # Tipo restrito ao protocolo Displayable
S = TypeVar('S', bound=Scorable)    # Tipo restrito ao protocolo Scorable

class TypedCollection(Generic[T]):
    """Versão Genérica da coleção do Lab 02 com anotações de tipos completas."""
    
    def __init__(self) -> None:
        self._items: List[T] = []

    def add(self, item: T) -> None:
        """Adiciona um item validando o tipo T."""
        self._items.append(item)

    def remove(self, item: T) -> None:
        """Remove um item da coleção."""
        self._items.remove(item)

    def get_all(self) -> List[T]:
        """Retorna todos os elementos como uma lista de T."""
        return list(self._items)

    # --- MÉTODOS NOTA 4 ---
    def find(self, predicate: Callable[[T], bool]) -> Optional[T]:
        """Retorna o primeiro elemento que satisfaz a condição ou None."""
        for item in self._items:
            if predicate(item):
                return item
        return None

    def filter(self, predicate: Callable[[T], bool]) -> List[T]:
        """Retorna uma lista de elementos do tipo T que satisfazem a condição."""
        return [item for item in self._items if predicate(item)]

    def map(self, transform: Callable[[T], R]) -> List[R]:
        """Aplica transformação e retorna lista de um NOVO tipo R."""
        return [transform(item) for item in self._items]

    def __len__(self) -> int:
        return len(self._items)
