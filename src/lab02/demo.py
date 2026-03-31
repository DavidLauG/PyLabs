import sys
import os

# Adiciona a raiz do projeto (PyLabs) ao sys.path para que o import 'src.lab01' funcione
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from src.lab01.model import Product
from collection import ProductCatalog

def run_demo():
    print("=== PROLTCH ANGOLA - GESTÃO DE INVENTÁRIO (LAB 02) ===\n")
    catalog = ProductCatalog()

    # 1. Criação de Dados Base
    p1 = Product("Laptop", "Thinkpad", 1200.0, 10)
    p2 = Product("Mouse", "Logitech", 50.0, 0) # Sem stock
    p3 = Product("Monitor", "Dell 27", 350.0, 5)
    p4 = Product("Teclado", "Keychron", 150.0, 15)

    # --- CENÁRIO 1: Integridade e Indexação ---
    print("--- Cenário 1: Adição e Proteção de Duplicados ---")
    catalog.add(p1)
    catalog.add(p2)
    catalog.add(p3)
    catalog.add(p4)
    # Tentativa de duplicado (mesmo nome e modelo)
    p_dup = Product("Laptop", "Thinkpad", 1000.0, 1)
    catalog.add(p_dup) 
    
    print(f"\nItem no índice 2: {catalog[2].name}") # __getitem__
    print(f"Total de itens: {len(catalog)}") # __len__

    #--- CENÁRIO 2: Filtros e Novas Coleções ---
    print("\n--- Cenário 2: Filtros Lógicos (Ativos e Preço) ---")
    p2.deactivate() # Inativamos o mouse
    
    active_ones = catalog.get_active()
    print(f"Produtos Ativos:\n{active_ones}")
    
    expensive_ones = catalog.get_expensive_products(300.0)
    print(f"\nProdutos Premium (>300 RUB):\n{expensive_ones}")

    # --- CENÁRIO 3: Ordenação e Gestão de Stock ---
    print("\n--- Cenário 3: Ordenação e Remoção ---")
    catalog.sort_by_price(reverse=True) # Mais caro primeiro
    print("Catálogo Ordenado por Preço (Descendente):")
    for p in catalog: # __iter__
        print(f"-> {p}")
    
    catalog.remove_at(0) # Remove o mais caro
    print(f"\nCatálogo após remoção do índice 0:\n{catalog}")

if __name__ == "__main__":
    run_demo()
