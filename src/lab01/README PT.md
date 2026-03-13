# ЛР-1 — Класс и инкапсуляция (Python 3.x)

# PARTE TEÓRICA E EXPLICAÇÃO DO PROJECTO
Este repositório contém a implementação rigorosa da primeira unidade laboratorial, focada em Programação Orientada a Objetos e Separação de Preocupações.
## Requisitos de Destaque (Variante 3)
1. **Encapsulamento Total:** Atributos privados e acesso via @property.
2. **Atributo de Classe:** store_name gerido ao nível da classe.
3. **Auditoria de Duplicados:** O método mágico __eq__ foi personalizado para emitir um Warning visual sempre que dois produtos com o mesmo Nome e Modelo são comparados.
4. **Gestão de Estado:** Bloqueio de operações (vendas/descontos) em produtos inativos.
## Descrição do Projeto
Este projeto é um exemplo prático de Programação Orientada a Objetos (POO), estruturado em três pilares fundamentais:
* **Classes e Instâncias:** A classe Product atua como o molde que define as regras, enquanto os objetos no inventory (como p1 e p2) são as instâncias reais com dados específicos.
* **Encapsulamento e Propriedades:** Os dados são protegidos por atributos privados (_price, _stock). O acesso é controlado por Getters (@property) e Setters, que garantem que nenhuma alteração de preço ou stock viole as regras de negócio, utilizando funções de validação externas para manter o código limpo.
* **Estado e Métodos Mágicos:** O objeto possui um Estado Lógico (_is_active) que bloqueia ou permite ações como vendas e descontos. Além disso, o uso de Métodos Mágicos (__eq__, __str__) permite que o Python trate os produtos de forma inteligente, disparando avisos automáticos de duplicados durante comparações.

## Arquitetura do Projeto
O projeto foi estruturado de forma modular:

**src/libraries/validation.py:** Motor de validação independente. Contém funções puras para validar strings, números e comprimentos mínimos.

**src/lab01/model.py:** Classe Product que implementa o domínio da Loja Online. Utiliza as funções do validation.py para garantir a integridade dos dados sem duplicar lógica.

**src/lab01/demo.py:** Script de demonstração que executa cenários de erro, gestão de estados e auditoria de inventário.



## VALIDATION.PY - src/libraries/validation.py
1. **validate_non_empty_string(value, field_name="Campo") -** Garante que o dado é texto e que não está "vazio" (apenas espaços). Aplicação: Nome do produto.
2. **validate_positive_number(value, field_name="Valor") -** Protege campos monetários ou medidas físicas. Aplicação: Preço do produto.
3. **validate_positive_int(value, field_name="Quantidade") -** Garante que quantidades sejam números inteiros e "naturais" (0, 1, 2...). Aplicação: Exclusivo para o Stock.
4. **validate_min_length(value, min_len, field_name="Texto") -** Garante que string tenha um mínimo de caractere considerável. Útil para evitar que alguém registe um modelo com apenas uma letra ou um código inválido.
Aplicação: Ideal para o Modelo (ex: exigir pelo menos 2 ou 3 caracteres).

*[Ver código competo de validation.py](../libraries/validation.py)*
## MODEL.PY - src/lab01/model.py
**1. O Construtor (__init__) e Encapsulamento**
* **Atributios privados:** O uso de _name, _price, etc., garante que os dados estão protegidos.
* **Validação Inicial:** Os dados são imediatamente validados. Caso não cumprir com os requisitos de validação, o objecto não será criado:
```Python
def __init__(self, name: str, model: str, price: float, stock: int):
        # Atributos de instância (4+1)
        self._name = validate_non_empty_string(name, "Nome")
        self._price = validate_positive_number(price, "Preço")
        self._stock = validate_positive_int(stock, "Stock")
        self._model = validate_min_length(model, 3, "Modelo")
        self._is_active = True
```
**2. Propriedades e Setters (@property)**
* **Controlo de Acesso:** Permite que o utilizador veja o preço e o stock, podendo alterar apenas o preço.
* **Integridade no Setter:** O @price.setter garante que, se o usuário tentar mudar o preço a meio do programa, a regra de "número positivo" continua a ser verificada.
```Python
# --- property (Getters e Setters) Свойства (@property) для чтения---
    @property
    def name(self):
        return self._name #Gets the name of the product

    @property
    def price(self):
        return self._price #Gets the price of the product

    @price.setter
    def price(self, value):
        # Utiliza a função externa de validação
        self._price = validate_positive_number(value, "Preço") #Sets the price of the product, but validating its price

    @property
    def stock(self):
        return self._stock #Gets the stock of the product
    
    @property
    def model(self): return self._model #Gets the model of the product
    
    @property
    def is_active(self):
        return self._is_active #Gets the status of the product
```
**3. Métodos Mágicos ("Identidade" do Objeto)**
* **__str__ vs __repr__:** O primeiro entrega uma linha bonita para o utilizador (com a moeda RUB e status do prooduto), o segundo entrega a estrutura técnica para o programador.
* **__eq__ com Alerta:** Ao comparar dois produtos, o sistema ativamente avisa sobre duplicados na consola.
```Python
# Métodos Mágicos
    def __str__(self): #OUTPUT FOR USERS
        status = "ATIVO" if self._is_active else "INATIVO"
        return f"{self._name} | model: {self._model} | {self._price:.2f} RUB | Stock: {self._stock} [{status}]"

    def __repr__(self): #OUTPUT FOR DEVELOPERS
        return f"Product('{self._name}', {self._model}, {self._price}, {self._stock})"

    def __eq__(self, other): #COMPARING IF 2 PRODUCTS ARE EQUALS IN NAME AND MODEL
        if not isinstance(other, Product): return False
        is_equal = (self._name.lower() == other._name.lower() and #Name
                    self._model.lower() == other._model.lower()) #Model
        if is_equal: #Warning if found equals products, it is, if "is_equal is true"
            print(f"⚠️ [WARNING]: O produto '{self._name}' ({self._model}) é idêntico ao produto comparado!")
        return is_equal
```
**4. Métodos de Negócio e Estado (Lógica de Fluxo)**
* **activate / deactivate:** Gerem o "ciclo de vida" do produto. O produto pode ser activado/desactivado manualmente. Não se colocou a opção automática de activação/desactivação para não se ter um código muito extenso. Mas a lógica seria verificar o valor de sctock: Se stock=0, então produto fica desactivado automáticamente; Esta verificação é feita sempre depois de uma venda. Se o utilizador quiser activar um produto, o sistema só activará caso stock>=1, esta validação pode ser feita dentro da função activate().
* **Dependência de Estado:** Os métodos sell e apply_discount funcionam om condições. Eles verificam primeiro se o produto está ativo. O método sell também só permite a venda caso haver stock e se a quantidade desejada não é maior que a do stock. O método apply_discount utiliza verificação simples, vendo apenas se se inseriu um número maior que zero e menor que 100. Poderia tamém se analizar desconto por cartão, ou por épocas de desconto (blackfriday, ou aniversário da loja ou cliente, por exemplo). Estas verificações são necessárias para impedir erros graves, como vender um item que foi retirado de catálogo.
* **Feedback Detalhado:** As mensagens de erro explicam ao utilizador o que fazer (ex: "Use a função activate()"), o que é uma excelente prática de design de software.
```Python
#   # Métodos de Negócio e Estado
def deactivate(self):
        self._is_active = False
        print (f"Product \"{self._name}, {self._model}\"  deactivated!!!. To activate use funtion activate()")

    def activate(self):
        self._is_active = True
        print (f"Product \"{self._name}, {self._model}\"  activated!!!. To deactivate use funtion deactivate()")

    def apply_discount(self, percentage: float):
        """
            Método de negócio com condicional de estado.
            Бизнес-метод с условным статусом.
        """
        if not self._is_active:
            print(f"Error: It is not possible to apply a discount to an inactive product.")
            return
        
        if 0 < percentage < 100:
            discount_amount = self._price * (percentage / 100)
            self._price -= discount_amount
            print(f"Descount of {percentage}% applied to the product \"{self._name}, {self._model}\". New price: {self._price:.2f}₽")
        else:
            print("Неверный процент скидки. Допустимый процент: 0 - 100")

    def sell(self, quantity: int):
        if not self._is_active:
            print(f"Error: The product \"{self._name}, {self._model}\" is deactivated. The sale cannot be completed.", end=" ")
            print(f"Enable the product so you can make the sale.")
            return
        
        if quantity > self._stock or self._stock==0:
            print(f"Error: Insufficient stock to sell {quantity} units.")
        else:
            self._stock -= quantity
            print(f"Sale completed: {quantity} units of \"{self._name}, {self._model}\".", end=" ")
            print(f"Now there are {self._stock} units of \"{self._name}, {self._model}\".")
```
*[Ver código competo de model.py](model.py)*
## DEMO.PY - src/lab01/demo.py
**1. Testes de Stress (Validação e Robustez)**
* **Blocos try/except:** Em vez de o programa "crashar", ele retornará erros específicos (nome vazio, modelo curto, preço negativo, stock negativo) para provar que o ficheiro *[validation.py](../libraries/validation.py)* está a proteger a classe Product.
```Python
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
```
![test validation](../../images/lab01/teste_validação.png)

**2 . Auditoria de Inventário (O Coração da Lógica)**
* **Iventário com ciclo for aninhado:** Ao percorrer a lista inventory comparando cada item com os seguintes, o programa gera um cenário real de controlo de qualidade, verificando quais produto são iguais em nome e modelo.
* **Interação com __eq__:** o comando "if inventory[i] == inventory[j]", faz com que o Python executae automaticamente o código que escrito em *[model.py](model.py)*, disparando o Warning e a sugestão de unificar stock. Isto automatiza a gestão da loja.
```Python
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
```
![comparação de produtos](../../images/lab01/comparação%20de%20produtos.png)

**3. Perspectivas de Visualização**
* **Vista Utilizador vs. Programador:** Para uma visualização estilosa e compreensivel para o utilizador, usamos o __str__ (legível e com moeda), e para o desenvolvedor, usamos o __repr__ (técnico). Isso ajuda muito na depuração de grandes sistemas.
```Python
    print(f"==================\nProdutos Criados: \n{p1}\n{p2}\n{p3}\n") #Vista Usuário
    print(f"==================\nProdutos Criados (Para desenvolvedor): \n{repr(p1)}\n{repr(p2)}\n{repr(p3)}") #Vista programador
```
![Listagem de produtos](../../images/lab01/Listagem%20de%20produtos.png)

**4. Ciclo de Vida e Regras de Negócio**
* **Teste de Fluxo:** Fez-se a simulação de uma sequência real: desativar -> tentar vender (bloqueio) -> ativar -> vender com sucesso.
* **Limite de Dados:** O teste de p1.sell(10) prova que o sistema respeita a quantidade física disponível, não permitindo vendas "fantasmas".
* **Atributos de Classe:** O fecho do código mostra que o nome da loja é consistente, quer o seja consultado através da planta geral, isto é, via classe (Product.store_name) ou de um objeto específico (p3.store_name).
```Python
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
    print(f"Via Class: {Product.store_name}")
    print(f"Via Instance p3: {p3.store_name}")
    print(f"\n==================\nProdutos: \n{p1}\n{p2}\n{p3}")
```
![Realização de Negócios](../../images/lab01/Realização%20de%20Negócios.png)

**5. Manipulação de Atributos de Classe e Instância**
* **Atributos de Classe:** A alteração do atributo de classe a partir da própria classe faz com que todas as instâncias sejam afetadas com esta alteração. É considerada como "Alteração global".
* **Atributos de Instância:** A alteração do atributo de classe a partir de uma instância (objecto) de classe faz com que as alterações fiquem somente neste objecto, sem afetar os outros objectos. É considerada como "Alteração local". No porjecto, foi testada a alteração do nome da loja usando o atributo de classe e de instância.
através da planta geral, isto é, via classe (Product.store_name) ou de um objeto específico (p3.store_name).
```Python
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
```
![Manipulação dos atributos locais e globais](../../images/lab01/Manipulação.png)

*[Ver código competo de demo.py](demo.py)*