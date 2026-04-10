"""
Этот файл служит связующим звеном между лабораторными работами 01 и 03,
    определяя общий интерфейс, необходимый для чистого полиморфизма.
    Este ficheiro atua como a ponte entre o Lab 01 e o Lab 03,
    definindo a interface comum necessária para o polimorfismo puro.
"""
import sys
import os

# Garante que o Python encontre a raiz do projeto para importar o Lab 01 e Lab 02
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from src.lab01.model import Product

class BaseProduct(Product):
    """
    Общий интерфейс для лабораторной работы № 03.
    Определяет метод get_details(), который станет основой для полиморфизма.
    Interface comum para o Lab 03. 
    Define o método get_details() que será a base do polimorfismo.
    """
    def get_details(self) -> str: #Метод, который необходимо переопределить в подклассах.
        # Método a ser sobrescrito nas subclasses
        return f"{self.name} ({self.model})"

    def display_info(self):
        # Exibe as informações formatadas de qualquer tipo de produto
        print(f"INFO: {self.get_details()} | Preço: {self.price:.2f} RUB")
