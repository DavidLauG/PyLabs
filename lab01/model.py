class Product:
    # Atributo de classe
    store_name = "Tech Store Python"

    def __init__(self, name: str, price: float, stock: int):
        # Atributos privados
        self._name = self._validate_name(name)
        self._price = self._validate_price(price)
        self._stock = self._validate_stock(stock)
        self._is_active = True  # Estado lógico

    # --- Métodos de Validação ---
    def _validate_name(self, name):
        if not isinstance(name, str) or len(name.strip()) == 0:
            raise ValueError("O nome deve ser uma string não vazia.")
        return name.strip()

    def _validate_price(self, price):
        if not isinstance(price, (int, float)) or price < 0:
            raise ValueError("O preço deve ser um número positivo.")
        return float(price)

    def _validate_stock(self, stock):
        if not isinstance(stock, int) or stock < 0:
            raise ValueError("O stock deve ser um número inteiro não negativo.")
        return stock

    # --- Propriedades (Getters e Setters) ---
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

    # --- Métodos Mágicos ---
    def __str__(self):
        status = "Ativo" if self._is_active else "Inativo"
        return f"Produto: {self._name} | Preço: {self._price:.2f}€ | Stock: {self._stock} [{status}]"

    def __repr__(self):
        return f"Product(name='{self._name}', price={self._price}, stock={self._stock})"

    def __eq__(self, other):
        if not isinstance(other, Product):
            return False
        return self._name == other._name and self._price == other._price

    # --- Métodos de Negócio ---
    def deactivate(self):
        """Altera o estado do objeto."""
        self._is_active = False
        print(f"O produto '{self._name}' foi desativado.")

    def apply_discount(self, percentage: float):
        """Método de negócio com condicional de estado."""
        if not self._is_active:
            print(f"Erro: Não é possível aplicar desconto num produto inativo.")
            return
        
        if 0 < percentage < 100:
            discount_amount = self._price * (percentage / 100)
            self._price -= discount_amount
            print(f"Desconto de {percentage}% aplicado. Novo preço: {self._price:.2f}€")
        else:
            print("Percentagem de desconto inválida.")

    def sell(self, quantity: int):
        """Método de negócio que depende do valor do stock."""
        if quantity <= self._stock:
            self._stock -= quantity
            print(f"Venda realizada: {quantity} unidades de {self._name}.")
        else:
            print(f"Erro: Stock insuficiente para vender {quantity} unidades.")
