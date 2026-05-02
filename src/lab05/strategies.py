"""Módulo de estratégias e funções de processamento para o Lab 05."""

# --- ESTRATÉGIAS DE ORDENAÇÃO (Nota 3) ---
def sort_by_name(product):
    """Ordena por nome de A-Z."""
    return product.name.lower()

def sort_by_price_asc(product):
    """Ordena por preço (mais barato primeiro)."""
    return product.price

def sort_by_stock_and_price(product):
    """Ordena por stock e depois por preço (Múltiplos atributos)."""
    return (product.stock, product.price)

# --- FÁBRICA DE FUNÇÕES (Nota 4) ---
def make_price_filter(max_price):
    """Cria um filtro personalizado para um preço máximo."""
    def filter_fn(product):
        return product.price <= max_price
    return filter_fn

# --- PADRÃO ESTRATÉGIA (CALLABLE OBJECTS) (Nota 5) ---
class DiscountStrategy:
    """Objeto chamável para aplicar descontos."""
    def __init__(self, percentage):
        self.percentage = percentage

    def __call__(self, product):
        """Aplica o desconto ao preço do produto."""
        discount = product.price * (self.percentage / 100)
        # Nota: Como o preço tem setter com validação, isto funciona bem
        product.price -= discount
        return product

class TechUpgradeStrategy:
    """Estratégia para 'melhorar' o modelo de produtos de TI."""
    def __call__(self, product):
        product._model = f"{product.model} [UPGRADED]"
        return product
