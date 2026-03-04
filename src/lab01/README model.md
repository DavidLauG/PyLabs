# ЛР-1 — Класс и инкапсуляция (Python 3.x)

# ПРАКТИЧЕСКАЯ ЧАСТЬ (Примеры кода с выводом результатов)
### *[Go to demo.py](demo.py)*
## Задание на 5, Вариант 3. 
```python
class Product:
    # Атрибут Класса
    store_name = "DGLinfo Store"

    def __init__(self, name: str, model: str, price: float, stock: int):
        # Личные Атрибуты
        self._name = self._validate_name(name)
        self._model = self._validate_model(model)
        self._price = self._validate_price(price)
        self._stock = self._validate_stock(stock)        
        self._is_active = True  # Логическое Состояние (Estado lógico)

    # --- Методы Валидации ---
    def _validate_name(self, name):
        if not isinstance(name, str) or len(name.strip()) == 0:
            raise ValueError("Имя должно быть непустой строкой.")
        return name.strip()

    def _validate_price(self, price):
        if not isinstance(price, (int, float)) or price <= 0:
            raise ValueError("Цена должна быть положительным числом.")
        return float(price)

    def _validate_stock(self, stock):
        if not isinstance(stock, int) or stock < 0:
            raise ValueError("Номер товара на складе должен быть неотрицательным целым числом.")
        return stock
    
    def _validate_model(self, model):
        if not isinstance(model, str) or len(model) < 3:
            raise ValueError("O modelo deve ter pelo menos 3 caracteres.")
        return model.strip()

    # --- property (Getters e Setters) Свойства (@property) для чтения---
    @property
    def name(self):
        return self._name

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = self._validate_price(value)

    @property
    def stock(self):
        return self._stock
    
    @property
    def model(self): return self._model
    
    @property
    def is_active(self):
        return self._is_active

    # --- Магические Методы ---
    def __str__(self):
        status = "Activated" if self._is_active and self._stock > 0 else "Deactivated"
        return f"Product: {self._name} | Model: {self._model} | Price: {self._price:.2f}₽ | Stock: {self._stock} [{status}]"

    def __repr__(self):
        return f"Product(name='{self._name}', model='{self._model}, price={self._price}, stock={self._stock})"

    def __eq__(self, other):
        if not isinstance(other, Product):
            return False
        return self._name.lower() == other._name.lower() and self._model.lower() == other._model.lower()

    # --- Métodos de Negócio / Методы Ведения Бизнеса ---
    def deactivate(self):
        """
            Altera o estado do objeto. Изменяет состояние объекта.
        """
        self._is_active = False
        print(f"Product '{self._name}' was deactivated.")

    def activate(self):
        """
            Altera o estado do produto para ativo.
            Изменяет статус продукта на активный.
        """
        self._is_active = True
        print(f"INFO: Product '{self._name}' is now activated.")
    
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
            print(f"Descount of {percentage}% applied to the product {self.name}. New price: {self._price:.2f}₽")
        else:
            print("Неверный процент скидки. Допустимый процент: 0 - 100")

    def sell(self, quantity: int):
        """
            Método de negócio que depende do valor do stock.
            Метод ведения бизнеса, основанный на стоимости товарных запасов.
        """
        if not self._is_active:
            print(f"Error: The product is deactivated. The sale cannot be completed.\n")
            print(f"Enable the product so you can make the sale.")
            return
        if quantity <= self._stock:
            self._stock -= quantity
            print(f"Sale completed: {quantity} units of {self._name}.")
        else:
            print(f"Error: Insufficient stock to sell {quantity} units.")

```