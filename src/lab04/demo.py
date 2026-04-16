import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from models import TechProduct, FreshProduct
from interfaces import IDisplayable, ISellable

# Nota 4: Função universal que trabalha com a INTERFACE, não com a classe
def print_service(item: IDisplayable):
    print(f"📠 RELATÓRIO: {item.get_info_formatted()}")

def run_demo():
    print("=== LAB 04: INTERFACES E CONTRATOS (NOTA 5) ===\n")

    # Lista mista de objetos que assinaram os contratos
    inventory = [
        TechProduct("VS Code", "Microsoft", 0.0, 999, "vscode.com", 200.0),
        FreshProduct("Banana", "Fazenda Sol", 15.0, 100, 4)
    ]

    # SCENARIO 1: Polimorfismo por Interface (Nota 5)
    print("--- Cenário 1: Uso de Função Universal (Interface) ---")
    for obj in inventory:
        print_service(obj) # Funciona para qualquer IDisplayable

    # SCENARIO 2: Verificação de Contrato (isinstance)
    print("\n--- Cenário 2: Verificação de Contratos ---")
    for obj in inventory:
        if isinstance(obj, ISellable):
            print(f"✅ {obj.name} pode ser vendido.")
        if isinstance(obj, IDisplayable):
            print(f"✅ {obj.name} pode ser impresso.")

    # SCENARIO 3: Venda via Interface
    print("\n--- Cenário 3: Venda Direta ---")
    for obj in inventory:
        obj.sell(5)

if __name__ == "__main__":
    run_demo()
