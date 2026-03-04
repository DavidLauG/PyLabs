from model import Product

def run_demo():
    print(f"--- Добро пожаловать в {Product.store_name} ---\n")
    print("--- Продукты ---")   
    
    # --- CENÁRIO 1: Criação das instâncias (Produtos) ---
    # --- СЦЕНАРИЙ 1: Создание экземпляров (продуктов) ---
    p1 = Product("Laptop Pro", "Lenovo-Thinkpad", 1200.0, 10)
    p2 = Product("Mouse RGB", "Logitech G502 X PLUS", 2669.0, 50)
    p3 = Product("Keyboard OLED", " Ajazz AK820 Pro", 24305.00, 50)
    p4 = Product("Laptop Pro", "Lenovo-Thinkpad", 25.0, 50)

    #  --- CENÁRIO 2: Criação e Validação de Erros ---
    #  --- СЦЕНАРИЙ 2: Создание и проверка ошибок ---
    print("\n--- Validation Test ---")
    try:
        invalid_product = Product("", "Lenovo-Thinkpad", 1200.0, 10)  # Empty name
    except ValueError as e:
        print(f"Captura de erro esperada: {e}")
    try:
        invalid_product = Product("Printer", "Lenovo-Thinkpad", 0.0, 10)  # Invalid price
    except ValueError as e:
        print(f"Captura de erro esperada: {e}")
    try:
        invalid_product = Product("Printer", "Lenovo-Thinkpad", 1200.0, -4)  # Invalid stock value
    except ValueError as e:
        print(f"Captura de erro esperada: {e}")
    
    #  --- CENÁRIO 3: Operações Normais e Métodos Mágicos ---
    #  --- СЦЕНАРИЙ 3: Обычные операции и магические методы ---
    print("\n--- Representation e Comparation ---")
    print(f"Product 1: {p1}") #__str__
    print(f"Product 2: {p2}")
    print(f"Product 3: {p3}")
    print(f"Product 4: {p4}")
    print(f"Reproduction: {repr(p2)}") #__repr__
    print(f"Товары p1 и p3 одинаковы (название/Модель)? {p1 == p3}") #__eq__
    print(f"Товары p1 и p4 одинаковы (название/Модель)? {p1 == p4}") #__eq__

    # --- CENÁRIO 4: Atributos de Classe ---
    # --- СЦЕНАРИЙ 4: Атрибуты класса ---
    print("\n--- Class Attributes ---")
    print(f"Via Class: {Product.store_name}")
    print(f"Via Instance p1: {p1.store_name}\n")

    # --- CENÁRIO 5: Lógica de Estado e Negócio ---
    # --- СЦЕНАРИЙ 5: Логика государства и бизнеса ---
    print("\n--- State Logic Test ---")
    p2.sell(10)      # Venda bem Sucedida / Успешная продажа
    # Aplicar desconto via Setter e Método
    # Примените скидку через Setter и Method.
    p1.price = 1400.0 # Alteração via Setter / Изменение через сеттер
    p1.apply_discount(25) # Aplica desconto / Примените скидку
    # Desativar e testar restrição / # Отключить и протестировать ограничение
    p1.deactivate()
    #Необходимо заблокировать его из-за логического состояния.
    p1.apply_discount(50) # Deve ser bloqueado pelo estado
    p1.sell(1)            # Deve ser bloqueado pelo estado
    
    # Testar limite de stock
    #
    p2.sell(100) # Deve avisar stock insuficiente
    print(f"\nFinal state of product 1: {p1}")
    print(f"Final state of product 2: {p2}")

if __name__ == "__main__":
    run_demo()
