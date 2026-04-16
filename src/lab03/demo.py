import sys
import os

# Ajuste de path para importar a coleção do Lab 02
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from src.lab02.collection import ProductCatalog
from models import DigitalProduct, PerishableProduct

def run_demo():
    print("=== PROLTCH ANGOLA - SISTEMA DE INVENTÁRIO HIERÁRQUICO (LAB 03) ===\n")
    
    catalog = ProductCatalog()

    # 1. Criação de objetos (Nota 3)
    p1 = DigitalProduct("PyCharm Pro", "JetBrains", 5000.0, 999, "://jetbrains.com", 850.5)
    p2 = DigitalProduct("Curso Python", "Udemy", 200.0, 1000, "://udemy.com", 1200.0)
    p3 = PerishableProduct("Computer", "HP-EliteBook", 45.0, 50, 3) # Próximo do vencimento    
    p4 = PerishableProduct("Computer", "Lenovo-Thinkpad", 1200.0, 10, 0) # Já vencido

    catalog.add(p1)
    catalog.add(p2)
    catalog.add(p3)
    catalog.add(p4)

    # --- CENÁRIO 1: Polimorfismo Puro (Nota 5) ---
    print("\n=== Сценарий 1: Полиморфная обработка (без IF) ===") #Processamento Polimórfico (Sem IFs)
    for item in catalog:
        # O mesmo método produz resultados diferentes dependendo do tipo do objeto
        print(f"-> {item.get_details()}")
        item.sell(1)
        print("-" * 20)

    # --- CENÁRIO 2: Filtros por Tipo (Nota 5) ---
    print("\n=== Сценарий 2: Фильтры по типу (только цифровые) ===") # Type Filters (Digital Only)
    # Uso de isinstance para filtrar a coleção
    digitals = [p for p in catalog if isinstance(p, DigitalProduct)]
    for d in digitals:
        print(f"Доступно для скачивания: {d.name} по ссылке {d.download_link}")

    # --- CENÁRIO 3: Métodos Específicos e super() (Nota 3 & 4) ---
    print("\n=== Сценарий 3: Проверка состояния и бизнес-правила ===")
    p3.check_expiration() # Método específico do Perishable
    p1.apply_discount(15) # Método herdado do Lab 01
    
    print("\n=== ОКОНЧАТЕЛЬНОЕ СОСТОЯНИЕ ИНВЕНТАРИЗАЦИИ ===")
    print(catalog)

if __name__ == "__main__":
    run_demo()
