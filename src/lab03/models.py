from base import BaseProduct

class DigitalProduct(BaseProduct): #classe filha
    def __init__(self, name: str, model: str, price: float, stock: int, download_link: str, file_size_mb: float):
        # Nota 3: Uso do super() e novos atributos
        #super() - envia os dados para a classe pai - class Product
        #Advantage: Automatic updates across all lab03: any update in lab01 affects lab03.
        super().__init__(name, model, price, stock)
        self.download_link = download_link #to download
        self.file_size_mb = file_size_mb #file size in MB

    # Nota 4: Sobrescrita de método de negócio (Polimorfismo)
    def sell(self, quantity: int):
        if not self.is_active:
            print(f"[ОШИБКА]: {self.name} неактивен.") #Se o produto não está activo
            return
        # Digital products do not reduce physical stock in the same way.
        print(f"Отправка доступа к: {self.download_link}") #Simulação de envio do link por email
        print(f"Продажа {quantity} лицензий '{self.name}' успешно завершена!") # Venda de "quantity" licença(s) de "protudo" realizada com sucesso!

    # Nota 5: Implementação polimórfica da interface comum
    #Polymorphism for "DigitalProduct" - the daughter returns her products as she wishes.
    def get_details(self) -> str:
        return f"[DIGITAL] {self.name} | {self.file_size_mb}MB | Link: {self.download_link}"

    #Inheritance and reuse - the daughter reuses the parent's __str__ and adds "[DIGITAL]"
    def __str__(self):
        return f"{super().__str__()} [Digital]"


class PerishableProduct(BaseProduct):
    def __init__(self, name: str, model: str, price: float, stock: int, expiry_days: int):
        super().__init__(name, model, price, stock)
        self.expiry_days = expiry_days

    # Nota 4: Sobrescrita com lógica condicional
    def sell(self, quantity: int):
        if self.expiry_days <= 0:
            print(f"[ПРОДАЖИ ЗАБЛОКИРОВАНЫ]: Срок действия товара '{self.name}' истек!")
            return
        #super() for override (Sobrescrita)- the daughter does what the father cannot do, in this case, checking the product's expiration date.
        super().sell(quantity)

    # Nota 3: Método exclusivo da classe filha
    def check_expiration(self):
        if self.expiry_days == 0:
            print(f"ВНИМАНИЕ: Срок действия товара '{self.name}' истек!!! Необходимо удалить!!!") # Produto já expirou.
        elif self.expiry_days < 5:
            print(f"ВНИМАНИЕ: Срок действия '{self.name}' истекает через {self.expiry_days} дней!") # faltam x dias para expirar
        else:
            print(f"'{self.name}' находится в пределах срока действия.") # dentro do prazo de validade

    # Nota 5: Implementação polimórfica da interface comum
    def get_details(self) -> str:
        return f"[СКОРОПОРТЯЩИЙСЯ ПРОДУКТ] {self.name} | Срок годности: {self.expiry_days} дней осталось"

    def __str__(self):
        return f"{super().__str__()} [Срок действия истек: {self.expiry_days}д]"
