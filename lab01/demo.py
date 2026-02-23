from model import Product

def run_demo():
    print(f"--- Bem-vindo à {Product.store_name} ---\n")

    # 1. Criação e print (__str__)
    p1 = Product("Laptop Pro", 1200.0, 10)
    p2 = Product("Mouse RGB", 25.0, 50)
    print(f"Produto 1: {p1}")
    print(f"Produto 2: {p2}")

    # 2. Comparação (__eq__)
    p3 = Product("Laptop Pro", 1200.0, 5)
    print(f"\nOs produtos p1 e p3 são iguais (nome/preço)? {p1 == p3}")

    # 3. Demonstração de Setter e Validação
    print("\n--- Testando Validação e Setters ---")
    try:
        p1.price = -50  # Deve falhar
    except ValueError as e:
        print(f"Captura de erro esperada: {e}")

    # 4. Métodos de Negócio e Estados
    print("\n--- Testando Lógica de Negócio ---")
    p2.sell(10)      # Venda normal
    p2.sell(100)     # Falha por falta de stock
    
    p1.apply_discount(10) # Aplica desconto
    p1.deactivate()       # Muda estado
    p1.apply_discount(5)  # Falha porque está inativo

    # 5. Atributo de Classe
    print(f"\nAcedendo atributo de classe via instância: {p1.store_name}")

if __name__ == "__main__":
    run_demo()
