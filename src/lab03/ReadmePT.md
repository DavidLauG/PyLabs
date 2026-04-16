# ЛР-3 — Наследование и иерархия классов

# Цель работы
* Освоить механизм наследования классов.
* Научиться строить иерархию объектов.
* Понять разницу между:
    * базовым классом
    * производным классом
* Научиться переиспользовать код.
* Освоить переопределение методов.

# 1. О проекте
O objetivo deste laboratório foi implementar os conceitos de Programação Orientada a Objetos (POO) avançada, focando em:
* **Herança:** Reutilização de lógica da classe base Product (Lab 01).
* **Polimorfismo:** Criação de uma interface comum onde diferentes objetos reagem ao mesmo método de formas distintas.
* **Encapsulamento:** Manutenção das regras de validação através da hierarquia.

# 2. Descrição da Hierarquia de Classes e Métodos
A estrutura foi organizada para evitar a duplicação de código e permitir a expansão do sistema:

* **Classe Base (Product):** contém os atributos fundamentais (nome, modelo, preço, stock).
* **Interface Intermediária (BaseProduct - base.py):** define o contrato get_details().
* **Classes Filhas (em models.py):**
    * **DigitalProduct:** Especializada em produtos intangíveis.
        * ``__init__:`` Utiliza o super() para inicializar os dados básicos.
        * ``sell()`` **(Sobrescrita/Polimorfismo):** Altera o comportamento original.
        + ``get_details()``: Implementa a interface comum.
        + ``__str__:`` Personaliza a exibição para o utilizador.
    * **PerishableProduct:** Especializada em bens de consumo.
        * ``__init__:`` Além dos dados base, inicializa o atributo ``expiry_days.``
        * ``sell()`` **(Sobrescrita/Polimorfismo):** Adiciona uma regra de negócio crítica: verifica se o produto está vencido. Se estiver, a venda é bloqueada. Caso contrário, utiliza super().sell() para seguir a lógica padrão de redução de stock.
        + ``check_expiration()`` **(Método Específico):** método exclusivo que analisa o risco de vencimento.
        + ``get_details()``: Implementa a interface comum focando na informação do prazo de validade restante.
        + ``__str__:`` Adiciona à visualização o estado da validade de forma legível.


# 3. Демонстрация проекта

##  --- Сценарий 1: Polimorfismo Puro ---
Iteração sobre uma lista mista em ``ProductCatalog``. Chamada de ``item.get_details()`` e ``item.sell()`` para todos.
+ **Resultado:** O sistema processa cada item corretamente sem usar blocos if/else para verificar o tipo. O comportamento é decidido pelo próprio objeto em tempo de execução.

![Listagem de produtos](../../images/lab03/cen01.png)

##  --- Сценарий 2: Filtros por Tipo ---
Utilizou-se a função ``isinstance()`` para extrair apenas produtos do tipo DigitalProduct da coleção global.
+ **Resultado:** Demonstra a integração entre a coleção do Lab 02 e a nova hierarquia.


![Listagem de produtos](../../images/lab03/cen02.png)

##  --- Сценарий 3: Super() e Métodos Específicos ---
Testou-se o uso de ``super().sell()`` no produto perecível para garantir que, se o produto estiver no prazo, a lógica original de redução de stock (do Lab 01) seja executada.
+ **Resultado:** Validação total da reutilização de código. 
![Listagem de produtos](../../images/lab03/cen03.png)

# 4. Conclusão
Através deste laboratório, foi possível compreender que a Herança não serve apenas para copiar código, mas para criar categorias lógicas. O Polimorfismo provou ser a ferramenta mais poderosa para manter o código limpo (Clean Code), permitindo que o catálogo de produtos cresça com novos tipos (ex: Service, Subscription) sem nunca precisar alterar o loop principal de vendas no demo.py.