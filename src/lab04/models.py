import sys
import os

# Ajuste de path para alcançar a raiz e o Lab 03
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from src.lab03.models import DigitalProduct, PerishableProduct # Reutilizando a base
from interfaces import ISellable, IDisplayable

# Nota 5: Software herda de DigitalProduct e assina ambos os contratos (Múltipla herança)
class SoftwareProduct(DigitalProduct, ISellable, IDisplayable): #Множественное наследование
    """
    DigitalProduct: Herda Identidade (Nome, Preço, Modelo) e a Lógica (enviar link por e-mail).
    ISellable: Assina o Contrato de Venda.
    IDisplayable: Assina o Contrato de Exibição Técnica.
    """    
    def get_technical_sheet(self) -> str:
        return f"[SOFTWARE] {self.name} | Versão: {self.model} | Requisitos: {self.file_size_mb}MB"

    # sell() herdado de DigitalProduct (envia link)

# Nota 5: Hardware (Perecível por depreciação/garantia)
class HardwareProduct(PerishableProduct, ISellable, IDisplayable):
    def __init__(self, name, model, price, stock, warranty_months):
        # Usamos expiry_days como meses de garantia para este exemplo
        super().__init__(name, model, price, stock, warranty_months)

    def get_technical_sheet(self) -> str:
        return f"[HARDWARE] {self.name} | Modelo: {self.model} | Garantia: {self.expiry_days} meses"
    
    # sell() herdado de PerishableProduct (bloqueia se a garantia/validade for 0)

# Este produto herda de DigitalProduct, mas NÃO herda de ISellable
class SystemPatch(DigitalProduct, IDisplayable):
    def get_technical_sheet(self) -> str:
        return f"[PATCH] {self.name} | Correção crítica de segurança."
    
    # Nota: Não incluímos ISellable na herança, logo ele não tem o método sell()
