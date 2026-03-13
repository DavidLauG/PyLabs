# ЛР-1 — Класс и инкапсуляция (Python 3.x)

# ТЕОРЕТИЧЕСКАЯ ЧАСТЬ И ОПИСАНИЕ ПРОЕКТА
В этом репозитории представлена строгая реализация первой лабораторной работы, которая посвящена Объектно-Ориентированному Программированию и разделению ответственности.

## Основные требования (Вариант 3)
1. **Полная инкапсуляция:** Приватные атрибуты и доступ через @property.
2. **Атрибут класса:** store_name управляется на уровне класса.
3. **Аудит дубликатов:** Магический метод __eq__ был изменен для вывода визуального предупреждения (Warning) каждый раз, когда сравниваются два товара с одинаковым Именем и Моделью..
4. **Управление состоянием:** Блокировка операций (продажа/скидка) для неактивных товаров.
## Описание проекта
Этот проект является практическим примером Объектно-Ориентированного Программирования (ООП), построенным на трех основных принципах:
* **Классы и экземпляры:**  Класс Product работает как шаблон, который определяет правила, в то время как объекты в inventory (например, p1 и p2) являются реальными экземплярами с конкретными данными.
* **Инкапсуляция и свойства:** Данные защищены приватными атрибутами (_price, _stock). Доступ контролируется с помощью геттеров (@property) и сеттеров, которые гарантируют, что изменение цены или остатка не нарушает бизнес-правила. Для чистоты кода используются внешние функции валидации.
* **Состояние и магические методы:** Объект имеет логическое состояние (_is_active), которое блокирует или разрешает такие действия, как продажа и скидка. Кроме того, использование магических методов (__eq__, __str__) позволяет Python обрабатывать товары умным способом, создавая автоматиче.

## Архитектура проекта
Проект имеет модульную структуру:

**src/libraries/validation.py:** Независимый механизм валидации. Содержит чистые функции для проверки строк, чисел и минимальной длины.

**src/lab01/model.py:** Класс Product, который реализует логику интернет-магазина. Использует функции из validation.py для обеспечения целостности данных без дублирования логики.

**src/lab01/demo.py:** Демонстрационный скрипт, который выполняет сценарии ошибок, управление состоянием и аудит инвентаря.

## VALIDATION.PY - src/libraries/validation.py
1. **validate_non_empty_string(value, field_name="Campo") -** Гарантирует, что данные являются текстом и не являются «пустыми» (только пробелы). Применение: Имя товара.
2. **validate_positive_number(value, field_name="Valor") -** Защищает денежные поля или физические показатели. Применение: Цена товара.
3. **validate_positive_int(value, field_name="Quantidade") -** Гарантирует, что количество является целым и «натуральным» числом (0, 1, 2...). Применение: Только для Stock (остаток).
4. **validate_min_length(value, min_len, field_name="Texto") -** Гарантирует, что строка имеет минимально допустимое количество символов. Полезно, чтобы никто не зарегистрировал модель только с одной буквой или неверным кодом.
Применение: Идеально для модели (например, требование минимум 2 или 3 символа).

*[Ver código competo de validation.py](../libraries/validation.py)*
## MODEL.PY - src/lab01/model.py
**1. Конструктор (init) и инкапсуляция**
* **Приватные атрибуты:** Использование _name, _price и т.д. гарантирует защиту данных.
* **Первоначальная валидация:** Данные проверяются немедленно. Если они не соответствуют требованиям валидации, объект не будет создан:
```Python
def __init__(self, name: str, model: str, price: float, stock: int):
        # Atributos de instância (4+1)
        self._name = validate_non_empty_string(name, "Nome")
        self._price = validate_positive_number(price, "Preço")
        self._stock = validate_positive_int(stock, "Stock")
        self._model = validate_min_length(model, 3, "Modelo")
        self._is_active = True
```
**2. Свойства и сеттеры (@property)**
* **Контроль доступа:** Позволяет пользователю видеть цену и остаток, но изменять можно только цену.
* **Целостность в сеттере:** @price.setter гарантирует, что если пользователь попытается изменить цену в середине программы, правило «положительного числа» все равно будет проверено.
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
**3. Магические методы («Личность» объекта)**
* **__str__ vs __repr__:** Первый метод создает красивую строку для пользователя (с валютой RUB и статусом товара), второй — техническую структуру для программиста.
* **__eq__ с предупреждением:** При сравнении двух товаров система активно сообщает о дубликатах в консоли.
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
**4. Бизнес-методы и состояние (Логика потока)**
* **activate / deactivate:** Управляют «жизненным циклом» товара. Товар можно активировать/деактивировать вручную. Мы не добавляли автоматическую активацию, чтобы код не был слишком длинным. Логика могла бы проверять остаток: если stock=0, товар деактивируется автоматически после продажи. Если пользователь хочет активировать товар, система сделает это только при stock>=1 (эту проверку можно сделать внутри функции activate()).
* **Зависимость от состояния:** Методы sell и apply_discount работают с условиями. Сначала они проверяют, активен ли товар. Метод sell также разрешает продажу только при наличии товара на складе и если желаемое количество не больше остатка. Метод apply_discount использует простую проверку: число должно быть больше нуля и меньше 100. Также можно было бы анализировать скидки по картам или сезонам (черная пятница, день рождения магазина и т.д.). Эти проверки необходимы для предотвращения серьезных ошибок, таких как продажа товара, который был удален из каталога.
* **Подробная обратная связь:** Сообщения об ошибках объясняют пользователю, что нужно сделать (например: «Используйте функцию activate()»), что является отличной практикой проектирования программного обеспечения.
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
**1. Стресс-тесты (Валидация и Надежность)**
* **Блоки try/except:** Вместо того чтобы программа завершалась с ошибкой («крашилась»), она будет возвращать специфические ошибки (пустое имя, короткая модель, отрицательная цена, отрицательный остаток). Это доказывает, что файл *[validation.py](../libraries/validation.py)* защищает класс Product.
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

**2 . Аудит инвентаря (Сердце логики)**
* **Инвентаризация с вложенным циклом for:** Проходя по списку inventory и сравнивая каждый элемент со следующими, программа создает реальный сценарий контроля качества, проверяя, какие товары имеют одинаковое имя и модель..
* **Взаимодействие с __eq__:** команда "if inventory[i] == inventory[j]", заставляет Python автоматически выполнять код, написанный в *[model.py](model.py)*, вызывая предупреждение (Warning) и предложение объединить остатки (stock). Это автоматизирует управление магазином.
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

**3. Перспективы визуализации**
* **Вид для пользователя и разработчика:** Для стильного и понятного отображения данных пользователю мы используем __str__ (читаемый текст с валютой), а для разработчика — __repr__ (технический формат). Это очень помогает при отладке больших систем..
```Python
    print(f"==================\nProdutos Criados: \n{p1}\n{p2}\n{p3}\n") #Vista Usuário
    print(f"==================\nProdutos Criados (Para desenvolvedor): \n{repr(p1)}\n{repr(p2)}\n{repr(p3)}") #Vista programador
```
![Listagem de produtos](../../images/lab01/Listagem%20de%20produtos.png)

**4. Жизненный цикл и бизнес-правила**
* **Тестирование потока:** Была проведена симуляция реальной последовательности: деактивация -> попытка продажи (блокировка) -> активация -> успешная продажа.
* **Лимит данных:** Тест p1.sell(10) доказывает, что система соблюдает доступное физическое количество, не позволяя совершать «фиктивные» продажи.
* **Атрибуты класса:** Завершение кода показывает, что название магазина остается неизменным, независимо от того, запрашивается ли оно через общий шаблон (напрямую через класс Product.store_name) или через конкретный объект (p3.store_name).
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

**5. Манипуляция атрибутами класса и экземпляра**
* **Атрибуты класса:** Изменение атрибута класса через сам класс влияет на все его экземпляры. Это считается «глобальным изменением».
* **Атрибуты экземпляра:** Изменение атрибута класса через конкретный экземпляр (объект) приводит к тому, что изменения отражаются только в этом объекте, не затрагивая остальные. Это считается «локальным изменением». В проекте было протестировано изменение названия магазина с использованием атрибута класса и атрибута экземпляра через общий шаблон, то есть через класс (Product.store_name) или через конкретный объект (p3.store_name).
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