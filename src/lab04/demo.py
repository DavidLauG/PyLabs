import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from src.lab02.collection import ProductCatalog
from models import SoftwareProduct, HardwareProduct, SystemPatch
from interfaces import IDisplayable, ISellable

# Função Universal: Trabalha com a Interface, não com a Classe
def generate_inventory_report(items: list[IDisplayable]):
    print("\n" + "="*50)
    print("      ТЕХНИЧЕСКИЙ ОТЧЕТ ПО ИТ-АКТИВАМ")
    print("="*50)
    for item in items:
        # Polimorfismo: Cada hardware ou software sabe imprimir sua ficha
        print(f"ЛИСТ: {item.get_technical_sheet()}")

def run_demo():
    catalog = ProductCatalog()

    # 1. Cadastro de Ativos de TI
    s1 = SoftwareProduct("Windows 11 Pro", "V.22H2", 1800.0, 500, "aka.ms/win11", 5000)
    h1 = HardwareProduct("Servidor Dell PowerEdge", "R750", 45000.0, 5, 36) # 36 meses garantia
    s2 = SoftwareProduct("Adobe Creative Cloud", "2024", 350.0, 100, "://adobe.com", 2500)
    h2 = HardwareProduct("Monitor antigo", "CRT-90", 50.0, 2, 0) # Sem garantia/obsoleto
    patch = SoftwareProduct("Security Update KB500", "Win11", 0.0, 0, "link.com", 150)

    catalog.add(s1); catalog.add(h1); catalog.add(s2); catalog.add(h2)

    # --- CENÁRIO 1: Polimorfismo via Interface (РАБОТА С ИНТЕРФЕЙСАМИ) ---
    # Pegamos tudo que é "Exibível" (IDisplayable)
    tech_items = [p for p in catalog if isinstance(p, IDisplayable)]
    generate_inventory_report(tech_items)

    # --- CENÁRIO 2: Regras de Negócio por Contrato (ISellable) ---
    # ПРАВИЛА БИЗНЕСА ПО ДОГОВОРУ КОНТРАКТУ
    print("\n--- ОБРАБОТКА ПРОДАЖ ИТ-ПРОДАЖ ---")
    vendas = [p for p in catalog if isinstance(p, ISellable)]
    for item in vendas:
        item.sell(1) # O software envia link, o hardware reduz stock (se tiver garantia)

    # --- CENÁRIO 3: Múltipla Implementação - ПРОВЕРКА ИНТЕРФЕЙСА---
    patch = SystemPatch("Security Update KB500", "Win11", 0.0, 0, "link.com", 150)
    print(f"\nПроверка контракта: {h1.name}")
    print(f"Реализует ли он функцию ISellable? {'Sim' if isinstance(h1, ISellable) else 'Não'}") #Retornará True
    print(f"Реализует ли он функцию IDisplayable? {'Sim' if isinstance(h1, IDisplayable) else 'Não'}") #Retornará True
    print(f"\nПроверка контракта: {patch.name}")
    print(f"Реализует ли он функцию IDisplayable? {isinstance(patch, IDisplayable)}") # Retornará True
    print(f"Реализует ли он функцию ISellable? {isinstance(patch, ISellable)}") # Retornará FALSE

if __name__ == "__main__":
    run_demo()
