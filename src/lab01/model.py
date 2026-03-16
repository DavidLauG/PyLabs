import sys
import os

# Adiciona o caminho para importar da pasta lib
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from libraries.validation import*

class Product:
    store_name = ""

    def __init__(self, name: str, model: str, price: float, stock: int):
        # Atributos de instância (4+1)
        self._name = validate_non_empty_string(name, "Nome")
        self._price = validate_positive_number(price, "Preço")
        self._stock = validate_positive_int(stock, "Stock")
        self._model = validate_min_length(model, 3, "Modelo")
        self._is_active = True
    
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

    # Métodos de Negócio e Estado
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