# ЛР-5 — Функции как аргументы. Стратегии и делегаты

# 1. Цель работы
+ Dominar a passagem de funções como argumentos para outras funções e métodos.
+ Aprender a usar funções de ordem superior integradas: ``map``, ``filter`` e ``sorted``.
+ Compreender o conceito do padrão Strategy e implementa-lo em Python.
+ Dominar expressões ``lambda`` e sua aplicação prática.
+ Integrar o estilo funcional com o código orientado a objetos dos LRs anteriores.

# 2. О проекте
O objetivo principal deste lab é tornar o catálogo de produtos flexível, permitindo que comportamentos (como ordenação, filtragem e modificação) sejam injetados externamente através de funções, expressões lambda e objetos chamáveis (Callables).

## I. Funções de Ordem Superior (Higher-Order Functions)
* ``filter():`` Utilizado para criar sub-coleções baseadas em critérios lógicos.
+ ``map():`` Utilizado para transformar dados ou aplicar ações em massa (como descontos).
+ ``sorted():`` Utilizado para ordenar o catálogo sem destruir a lista original.

## II. Estratégias de Classificação (``strategies.py``)
Funções utilizadas como critério para organizar o catálogo:
* ``sort_by_name:`` Converte o nome para minúsculas e ordena de A a Z.
+ ``sort_by_price_asc:`` Organiza os produtos do menor para o maior preço.
+ ``sort_by_stock_and_price:`` Ordena primeiro pela quantidade em stock e, em seguida, pelo preço.

## III. Funções de Filtragem
Critérios para selecionar subconjuntos de produtos:
+ ``filter_by (lambda):`` Filtros rápidos (``ex: p.price > 100``) definidos na execução.
+ ``isinstance (Filtro de Tipo):`` Filtra produtos por categoria (ex: apenas ``SoftwareProduct``).

## IV. Fábrica de Funções (Closures)
Funções que geram outras funções personalizadas:
´``make_price_filter(max_price):`` Cria uma função que verifica se o preço de um produto está abaixo de um limite específico.

## V. Objetos Chamáveis (Strategy Pattern)
Classes que mantêm estado e podem ser chamadas como funções:
+ ``DiscountStrategy(percentage):`` Calcula e aplica uma redução percentual no preço dos produtos.
+ ``TechUpgradeStrategy():`` Altera a string do modelo do produto para marcar uma atualização técnica.

## VI. Métodos de Ordem Superior (``collection.py``)
Métodos do ``AdvancedProductCatalog`` que processam a coleção:
+ ``filter_by(predicate):`` Retorna um novo catálogo contendo apenas os itens que satisfazem uma condição.
+ ``sort_by_strategy(key_func):`` Gera uma versão ordenada do catálogo baseada numa estratégia de chave.
+ ``apply(func):`` Aplica uma transformação ou ação a todos os produtos da lista original.
+ ``get_names_list():`` Usa ``map`` para extrair apenas os nomes dos produtos da coleção.

# 3. Демонстрация проекта (demo.py)

##  --- Cenário 1: Mesclagem Sequencial (Filtrar > Classificar > Aplicar) ---
![Listagem de produtos](../../images/lab05/cen01.png)

##  --- Cenário 2: Fábrica de Filtros e Mapa de Nomes ---

![Listagem de produtos](../../images/lab05/cen02.png)

##  --- Cenário 3: Alterando a estratégia de descontos ---
![Listagem de produtos](../../images/lab05/cen03.png)

# 4. Conclusão
O uso de programação funcional permitiu criar um sistema onde o **"o quê fazer"** (Catálogo) está separado do **"como fazer"** (Estratégias), facilitando a manutenção e a expansão do software.