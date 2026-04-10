from base import BaseProduct

class DigitalProduct(BaseProduct):
    def __init__(self, name: str, model: str, price: float, stock: int, download_link: str, file_size_mb: float):
        # Nota 3: Uso do super() e novos atributos
        super().__init__(name, model, price, stock)
        self.download_link = download_link
        self.file_size_mb = file_size_mb

    # Nota 4: Sobrescrita de método de negócio (Polimorfismo)
    def sell(self, quantity: int):
        if not self.is_active:
            print(f"❌ [ERRO]: {self.name} está inativo.")
            return
        # Produtos digitais não reduzem stock físico no mesmo sentido
        print(f"📧 Enviando acesso para: {self.download_link}")
        print(f"✅ Venda de {quantity} licença(s) de '{self.name}' realizada com sucesso!")

    # Nota 5: Implementação polimórfica da interface comum
    def get_details(self) -> str:
        return f"[DIGITAL] {self.name} | {self.file_size_mb}MB | Link: {self.download_link}"

    def __str__(self):
        return f"💾 {super().__str__()} [Digital]"


class PerishableProduct(BaseProduct):
    def __init__(self, name: str, model: str, price: float, stock: int, expiry_days: int):
        super().__init__(name, model, price, stock)
        self.expiry_days = expiry_days

    # Nota 4: Sobrescrita com lógica condicional
    def sell(self, quantity: int):
        if self.expiry_days <= 0:
            print(f"⚠️ [VENDAS BLOQUEADAS]: O produto '{self.name}' expirou!")
            return
        super().sell(quantity)

    # Nota 3: Método exclusivo da classe filha
    def check_expiration(self):
        if self.expiry_days < 3:
            print(f"📢 AVISO: '{self.name}' vence em {self.expiry_days} dias. Considerar promoção!")
        else:
            print(f"✅ '{self.name}' está dentro do prazo de validade.")

    # Nota 5: Implementação polimórfica da interface comum
    def get_details(self) -> str:
        return f"[PERECÍVEL] {self.name} | Validade: {self.expiry_days} dias restantes"

    def __str__(self):
        return f"🍎 {super().__str__()} [Exp: {self.expiry_days}d]"
