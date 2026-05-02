import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from src.lab04.models import SoftwareProduct, HardwareProduct
from collection import AdvancedProductCatalog
import strategies as st

def run_demo():
    print("=== LAB 05: PROGRAMAÇÃO FUNCIONAL E ESTRATÉGIAS (NOTA 5) ===\n")

    catalog = AdvancedProductCatalog()

    # 1. Criação de Dados
    catalog.add(SoftwareProduct("Windows 11", "Pro", 1500.0, 100, "ms.com", 5000))
    catalog.add(HardwareProduct("Monitor Dell", "U2723QE", 4500.0, 10, 36))
    catalog.add(SoftwareProduct("Adobe PS", "2024", 300.0, 50, "adobe.com", 2000))
    catalog.add(HardwareProduct("Teclado RGB", "G915", 1200.0, 5, 12))
    catalog.add(HardwareProduct("Mouse Velho", "M100", 50.0, 20, 0))

    # --- CENÁRIO 1: Cadeia de Operações (Nota 5) ---
    print("\n--- Cenário 1: Encadeamento (Filtro > Ordenação > Aplicação) ---")
    # 1. Filtrar ativos (is_active)
    # 2. Ordenar por preço (lambda)
    # 3. Aplicar upgrade (estratégia callable)
    result = (catalog
              .filter_by(lambda p: p.price > 100)
              .sort_by_strategy(st.sort_by_price_asc)
              .apply(st.TechUpgradeStrategy()))

    print("Resultado da Cadeia:")
    print(result)

    # --- CENÁRIO 2: Fábrica de Funções e Map (Nota 4) ---
    print("\n--- Cenário 2: Fábrica de Filtros e Map de Nomes ---")
    price_filter_3000 = st.make_price_filter(3000)
    affordable_items = catalog.filter_by(price_filter_3000)
    
    print(f"Nomes dos itens até 3000 RUB: {affordable_items.get_names_list()}")

    # --- CENÁRIO 3: Substituição de Estratégias (Nota 5) ---
    print("\n--- Cenário 3: Troca de Estratégia de Desconto ---")
    summer_sale = st.DiscountStrategy(10) # 10% de desconto
    black_friday = st.DiscountStrategy(50) # 50% de desconto
    
    print("Aplicando 50% de desconto em tudo...")
    catalog.apply(black_friday)
    print(catalog)

if __name__ == "__main__":
    run_demo()
