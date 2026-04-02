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
            raise TypeError(f"Ошибка: Добавлять можно только объекты типа Product.") #Only can add objects of type Product
        
        # Restrição de Duplicados (Nota 4) - Usa o __eq__ do model.py
        if product in self._items: #Cannot repeat products (name and model)
            print(f"⚠️ [ОТКЛОНЕНО]: Товар '{product.name}' ({product.model}) уже существует в каталоге.")
            return
        
        self._items.append(product) #Add the new item
        print(f"✅ Добавлен товар: {product.name} ({product.model})")

    def get_all(self):
        """Retorna todos os produtos"""
        return self._items

    # --- MÉTODOS MÁGICOS (Nota 4 e 5) ---
    def __len__(self): #Permite usar len(catalogo)
        """Define o tamanho"""
        return len(self._items)

    def __iter__(self):
        """Permite usar for p in catalogo"""
        return iter(self._items)

    def __getitem__(self, index): #Permite usar catalogo[0] (Nota 5)
        """Retorna um produto no index desejado"""
        return self._items[index]

    # --- REMOÇÃO E BUSCA (Nota 4 e 5) ---
    def remove(self, item: Product) -> None:
        if item not in self._items:
            raise ValueError("Товар не найден в коллекции")
        self._items.remove(item)
        print(f"🗑️ Товар {item.name} удален!!!")

    def remove_at(self, index: int): #Remove por índice (Nota 5)
        """Remove an expecific product at desired index"""
        try:
            removed = self._items.pop(index)
            print(f"🗑️  Товар удален из индекса {index}: {removed.name}")
        except IndexError:
            print(f"❌ Ошибка: Индекс {index} не существует.")

    def find_by_name(self, name: str): #Busca por nome (Nota 4)
        """Find product by name"""
        for p in self._items:
            if p.name.lower() == name.lower():
                return p
        return None

    # --- ORDENAÇÃO E FILTROS (Nota 5) ---
    def sort_by_price(self, reverse=False): #Ordena a coleção atual por preço.
        """Sort the current collection by price."""
        self._items.sort(key=lambda p: p.price, reverse=reverse)
        print(f"⚖️ Каталог отсортирован по цене.")

    def get_active(self): #Retorna uma NOVA COLEÇÃO apenas com produtos ativos.
        """Returns a NEW COLLECTION with only active products."""
        active_items = [p for p in self._items if p.is_active] #Return all activated products
        return ProductCatalog(active_items)

    def get_expensive_products(self, min_price: float): 
        """A NEW COLLECTION is returning with products above a certain price point."""
        expensive_items = [p for p in self._items if p.price >= min_price]
        return ProductCatalog(expensive_items)

    def __str__(self):
        if not self._items:
            return "Каталог пуст."
        return "\n".join([f"[{i}] {p}" for i, p in enumerate(self._items)])
