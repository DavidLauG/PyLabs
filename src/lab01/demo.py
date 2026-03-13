from model import Product

def run_demo():
    print(f"--- {Product.store_name} ---\n")

    # Demonstração de Erro de Validação (Proveniente do lib/validators.py)
    print("\n--- Validation Test ---")
    try:
        invalid_product = Product("", "Lenovo-Thinkpad", 1200.0, 10)  # Empty name
    except ValueError as e:
        print(f"Captura de erro esperada: {e}") #Name cannot be empty
    try:
        invalid_product = Product("Printer", "   ", 1200.0, 10)  # Model's name
    except ValueError as e:
        print(f"Captura de erro esperada: {e}") #Model must have at least 3 chars    
    try:
        invalid_product = Product("Printer", "Lenovo-Thinkpad", -4, 10)  # Invalid price
    except ValueError as e:
        print(f"Captura de erro esperada: {e}") #Price must be at least 0 (means free product - eg, marketing blackfriday)
    try:
        invalid_product = Product("Printer", "Lenovo-Thinkpad", 1200.0, -4)  # Invalid stock value
    except ValueError as e:
        print(f"Captura de erro esperada: {e}") #stock must begin from 0

    # Demonstração de Sucesso e Estado
    inventory = [
        Product("Laptop Pro", "Lenovo-Thinkpad", 1200.0, 10),
        Product("Mouse RGB", "Logitech G502 X PLUS", 2669.0, 50),
        Product("Keyboard OLED", "Ajazz AK820 Pro", 24305.00, 50),
        Product("Laptop Pro", "Lenovo-Thinkpad", 1200.0, 10) # Duplicado (mesmo nome e modelo)
    ]
    print("\n--------Comparação de produtos-------------")
    for i in range(len(inventory)): #i pega os 4 elementos. A iteração começa com i=0
        for j in range(i + 1, len(inventory)): # j pega i+1 até 4-3, ou seja sai de i+1 até 3
            # O método __eq__ será chamado aqui e disparará o Warning se forem iguais
            if inventory[i] == inventory[j]: #Primeia iteração, por exemplo, compara se item[0]==item[1]
                print(f"   -> Ação sugerida: Unificar stock dos itens {i+1} e {j+1}.\n")#+1, por causa do utilizador.

    #Reorganização dos produtos, depois de haver feito a comparação em nome e modelo.
    p1 = inventory[0]  # Laptop Pro Lenovo-Thinkpad
    p2 = inventory[1]  # Mouse RGB Logitech G502 X PLUS
    p3 = inventory[2]  # Keyboard OLED Ajazz AK820 Pro

    print(f"==================\nProdutos Criados: \n{p1}\n{p2}\n{p3}\n") #Vista Usuário
    print(f"==================\nProdutos Criados (Para desenvolvedor): \n{repr(p1)}\n{repr(p2)}\n{repr(p3)}") #Vista programador

    
    print("\n------------2. Testando Comportamento de Estado:----------------")
    p1.deactivate()
    p1.sell(1) # Deve ser bloqueado por estar inativo
    p1.activate()
    p2.deactivate()
    p1.sell(2) # Deve funcionar agora
    p1.sell(10) # Deve falahar por insufiência de stock
    p1.apply_discount(-3) #Por questão de lógica, o desconto não pode ser realizado
    p1.apply_discount(20)
     # --- CENÁRIO 4: Atributos de Classe ---
    # --- СЦЕНАРИЙ 4: Атрибуты класса ---
    print("\n--- Class Attributes ---")
    
    # Alteração via atributo de classe, alteração global - afecta todo o projecto
    # - útil, por exemplo, quando se muda o nome da loja completa, junto com seus produtos.
    Product.store_name="PROLTCH ANGOLA, Lda" #Nome da loja mudado para "PROLTCH ANGOLA, Lda"
    # Alteração via atributo de instância, alteração local - afecta paneas o produto
    p1.store_name="David" #Produto p1 é de uma loja/fabricante diferente
    print(f"Via Class: {Product.store_name}") #PROLTCH ANGOLA, Lda
    print(f"Via Instance p3: {p3.store_name}") #PROLTCH ANGOLA, Lda
    print(f"Via Instance p1: {p1.store_name}") #David
    
    #Produts updated list/status
    print(f"\n==================\nProdutos: \n{p1}\n{p2}\n{p3}")

if __name__ == "__main__":
    run_demo()
