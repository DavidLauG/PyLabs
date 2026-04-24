class Product:
    def __init__(self, name: str, price: float):
        self._name = name
        self._price = price

    @property
    def name(self):
        return self._name

    def calculate_price(self) -> float:
        return self._price

    def __str__(self):
        return f"{self._name}: {self._price:.2f} руб."

# Ваш код:
class DigitalProduct(Product):
    def __init__(self, name: str, price: float, file_size_mb: float):
        super().__init__(name, price) # "talk" to class father - heritage
        self.file_size_mb = file_size_mb #file size in MB - adicional atribute
        #Validation
        if file_size_mb <= 0:
            raise ValueError("File zibe must be > 0.")
        self.file_size_mb = file_size_mb
    def calculate_price(self) -> float:
        if self.file_size_mb>100:            
            discount_amount = self._price * (10 / 100)
            self._price -= discount_amount
        return self._price
    def get_info(self) -> str:
        return f"[Digital] {self.name} ({self.file_size_mb} MB)"

#catalog = Product()
p1 = DigitalProduct("PyCharm Pro", 5000.0, 999)

p2 = DigitalProduct("PyCharm Pro", 5000.0, 50)

print(p1.calculate_price())
print(p2.calculate_price())

print(p1.get_info())