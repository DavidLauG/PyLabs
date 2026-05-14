# Python 3.12+
class Repositorio[T]:
    def __init__(self) -> None:
        self._itens: list[T] = []

    def adicionar(self, item: T) -> None:
        self._itens.append(item)

    def obter_todos(self) -> list[T]:
        return self._itens

repo_usuarios = Repositorio[str]()
repo_usuarios.adicionar("Alice")

print(repo_usuarios.obter_todos())