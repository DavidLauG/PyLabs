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
    p2 = Product("Mouse", "Thinkpad", 450.0, 0) # Without stock
    p3 = Product("Monitor", "Dell 27", 350.0, 5)
    p4 = Product("Keyboard", "Keychron", 1500.0, 15)
    p5 = Product("Printer", "HP-34", 150.0, 15)

    # --- CENÁRIO 1: Integridade e Indexação ---
    print("--- Сценарий 1: Добавление и защита дубликатов ---") #Cenário 1: Adição e Proteção de Duplicados
    catalog.add(p1)
    catalog.add(p2)
    catalog.add(p3)
    catalog.add(p4)
    catalog.add(p5)
    # Tentativa de duplicado (mesmo nome e modelo)
    p_dup = Product("Laptop", "Thinkpad", 1000.0, 1)
    catalog.add(p_dup) #Returns a duplicate product warning.
    
    print(f"\nТовар со 2-й позиции: {catalog[1].name}") # __getitem__ - mostra o produto no index "1" que é a 2ª posção
    print(f"Общее количество товаров: {len(catalog)}") # __len__ - mostra Número total de produtos:

    #--- CENÁRIO 2: Filtros e Novas Coleções ---
    print("\n--- Сценарий 2: Логические фильтры (активы и цена) ---") #
    #Activação/Desactivação e listagem
    p2.deactivate() # Desativa-se o mouse
    
    active_ones = catalog.get_active() #Get all the activated articles
    print(f"\nAtivated Products:\n{active_ones}")

    dactive_ones = catalog.get_deactive() #Get all the deactivated articles
    print(f"\nDeativated Products:\n{dactive_ones}")
    
    #Procura por nome e de forma geral
    find_product=catalog.find_by_name("Laptop") #Produto Existente
    print(f"\nТовар найден: {find_product}")
    find_product=catalog.find_by_name("Impressora") #Produto Não Existente
    print(f"\nТовар не найден: {find_product}")

    #Busca de forma global
    search_name = catalog.find_by("name", "Laptop") #Por nome
    print(f"\nРезультаты поиска по названию 'Laptop': {search_name if search_name else 'Нет'}")

    search_model = catalog.find_by("model", "Thinkpad").get_deactive() #Por modelo, mas apenas os desactivos
    print(f"\nРезультаты поиска по model 'Thinkpad' - deactivated only: {search_model if search_model else 'Нет'}")

    expensive_ones = catalog.get_expensive_products(300.0) #Pega todos os produtos com preço >=300
    print(f"\nPremium Products (>=300 RUB):\n{expensive_ones}")

    # --- CENÁRIO 3: Ordenação e Gestão de Stock ---
    print("\n--- Сценарий 3: Сортировка и удаление ---") #Ordenação e Remoção
    catalog.sort_by_price(reverse=True) # More expensive at first.
    for p in catalog: # __iter__
        print(f"-> {p}")

    catalog.sort_by("name") #Ordenar por nome
    print(f"{catalog}")

    """
    # Ordenar por Preço (Caro -> Barato)
    catalog.sort_by("price", reverse=True)
    print(f"\nOrdenado por Preço (Desc):")
    for p in catalog:
        print(f"-> {p.name}: {p.price} RUB")

    # Ordenar por Stock (Menor -> Maior)
    catalog.sort_by("stock")
    print(f"\nOrdenado por Stock:\n{catalog}")
    """

    print("\nProduct removal:\n")
    catalog.remove_at(6) # Erro!!! Индекс не существует
    catalog.remove_at(0) # Removed. Индекс существует
    catalog.remove(p5)
    print(f"\nКаталог после удаления индекса 0:\n{catalog}")

if __name__ == "__main__":
    run_demo()
