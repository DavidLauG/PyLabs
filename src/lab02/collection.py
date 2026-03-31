import sys
import os

# Garante que conseguimos importar o Product do lab01
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from src.lab01.model import Product

class ProductCatalog:
    def __init__(self, items=None):
        # Aceita uma lista inicial (útil para os filtros que retornam nova coleção)
        self._items = items if items is not None else []

    # --- GESTÃO BÁSICA (Nota 3) ---
    def add(self, product: Product):
        """Adiciona um produto validando o tipo e duplicados."""
        if not isinstance(product, Product):
            raise TypeError(f"Erro: Apenas objetos do tipo Product podem ser adicionados.")
        
        # Restrição de Duplicados (Nota 4) - Usa o __eq__ do model.py
        if product in self._items:
            print(f"⚠️ [REJEITADO]: O produto '{product.name}' ({product.model}) já existe no catálogo.")
            return
        
        self._items.append(product)
        print(f"✅ Adicionado: {product.name} ({product.model})")

    def get_all(self):
        return self._items

    # --- MÉTODOS MÁGICOS (Nota 4 e 5) ---
    def __len__(self):
        """Permite usar len(catalogo)"""
        return len(self._items)

    def __iter__(self):
        """Permite usar for p in catalogo"""
        return iter(self._items)

    def __getitem__(self, index):
        """Permite usar catalogo[0] (Nota 5)"""
        return self._items[index]

    # --- REMOÇÃO E BUSCA (Nota 4 e 5) ---
    def remove_at(self, index: int):
        """Remove por índice (Nota 5)"""
        try:
            removed = self._items.pop(index)
            print(f"🗑️ Removido do índice {index}: {removed.name}")
        except IndexError:
            print(f"❌ Erro: O índice {index} não existe.")

    def find_by_name(self, name: str):
        """Busca por nome (Nota 4)"""
        results = [p for p in self._items if p.name.lower() == name.lower()]
        return results if results else None

    # --- ORDENAÇÃO E FILTROS (Nota 5) ---
    def sort_by_price(self, reverse=False):
        """Ordena a coleção atual por preço."""
        self._items.sort(key=lambda p: p.price, reverse=reverse)
        print(f"⚖️ Catálogo ordenado por preço.")

    def get_active(self):
        """Retorna uma NOVA COLEÇÃO apenas com produtos ativos."""
        active_items = [p for p in self._items if p.is_active]
        return ProductCatalog(active_items)

    def get_expensive_products(self, min_price: float):
        """Retorna uma NOVA COLEÇÃO com produtos acima de um preço."""
        expensive_items = [p for p in self._items if p.price > min_price]
        return ProductCatalog(expensive_items)

    def __str__(self):
        if not self._items:
            return "O catálogo está vazio."
        return "\n".join([f"[{i}] {p}" for i, p in enumerate(self._items)])
