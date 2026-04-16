import sys
import os

# Ajuste de path para o Lab 03
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from src.lab03.models import DigitalProduct, PerishableProduct
from interfaces import ISellable, IDisplayable

# Nota 4 & 5: Implementação múltipla de interfaces
class TechProduct(DigitalProduct, ISellable, IDisplayable):
    def get_info_formatted(self) -> str:
        return f"[TECH-DIGITAL] {self.name} | Link: {self.download_link}"

    # O sell() já vem herdado do DigitalProduct, que agora cumpre o contrato ISellable

class FreshProduct(PerishableProduct, ISellable, IDisplayable):
    def get_info_formatted(self) -> str:
        return f"[FRESH-FOOD] {self.name} | Validade: {self.expiry_days} dias"
