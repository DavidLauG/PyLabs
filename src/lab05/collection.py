import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from src.lab02.collection import ProductCatalog

class AdvancedProductCatalog(ProductCatalog):
    """Extensão do catálogo com suporte a programação funcional e encadeamento."""

    def filter_by(self, predicate):
        """Filtra a coleção usando uma função booleana (Nota 4)."""
        filtered_items = list(filter(predicate, self._items))
        return AdvancedProductCatalog(filtered_items)

    def sort_by_strategy(self, key_func, reverse=False):
        """Ordena a coleção usando uma função de chave (Nota 4)."""
        # sorted() não altera a lista original, por isso criamos um novo catálogo
        sorted_items = sorted(self._items, key=key_func, reverse=reverse)
        return AdvancedProductCatalog(sorted_items)

    def apply(self, func):
        """Aplica uma função/estratégia a todos os elementos (Nota 5)."""
        # map() aplica a função a todos os itens
        self._items = list(map(func, self._items))
        return self # Retorna self para permitir encadeamento

    def get_names_list(self):
        """Exemplo de uso de map para extrair apenas nomes."""
        return list(map(lambda p: p.name, self._items))
