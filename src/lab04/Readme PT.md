# ЛР-4 — Интерфейсы и абстрактные классы (ABC)

# 1. Цель работы
Aprofundar os conceitos de **abstração** e **múltipla herança,** focando em:
+ **Classes Base Abstratas (ABC):** Definição de moldes que não podem ser instanciados diretamente.
+ **Interfaces:** Criação de contratos de comportamento obrigatórios.
+ **Múltipla Implementação:** Capacidade de uma classe assinar e cumprir múltiplos contratos simultaneamente.
+ **Polimorfismo via Interfaces:** Manipulação de objetos baseada no que eles "sabem fazer" e não no que eles "são".
# 2. О проекте
Neste laboratório, o sistema de inventário foi evoluído para um modelo de gestão de Ativos de TI, utilizando as seguintes interfaces:
## Interfaces (interfaces.py)
+ **ISellable:** obriga a implementação do método ``sell()``. Garante que apenas produtos comercializáveis sejam processados pelo sistema de vendas.
+ **IDisplayable:** obriga a implementação do método ``get_technical_sheet()``. Garante que cada ativo de TI forneça as suas especificações técnicas de forma padronizada.
## Classes de TI (models.py)
**Múltipla Herança** para combinar dados de labs anteriores com os novos contratos:
+ **SoftwareProduct:** Herda de ``DigitalProduct`` (Lab 03) e implementa ``ISellable`` e ``IDisplayable``. Foca em versões e links de download.
+ **HardwareProduct:** Herda de ``PerishableProduct`` (Lab 03) e implementa ``ISellable`` e ``IDisplayable``. Utiliza a lógica de expiração para representar a **Garantia Técnica.**
+ **SystemPatch** (Prova de Conceito): Herda apenas de ``IDisplayable``. Serve para demonstrar a filtragem negativa no sistema.

# 3. Демонстрация проекта (demo.py)

##  --- Сценарий 1: Interfaces como Tipos (POLIMORFISMO VIA INTERFACE) ---
![Listagem de produtos](../../images/lab04/cen01.png)

##  --- Сценарий 2: Filtros por Tipo ---

![Listagem de produtos](../../images/lab04/cen02.png)

##  --- Сценарий 3: Verificação de Interface ---
![Interface Validation](../../images/lab04/cen03.png)