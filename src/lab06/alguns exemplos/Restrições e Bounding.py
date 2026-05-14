from typing import TypeVar

# T deve ser obrigatoriamente str ou bytes (Constraints)
T_Text = TypeVar('T_Text', str, bytes)

def processar_texto(dados: T_Text) -> T_Text:
    return dados

# T_Num deve ser int, float ou qualquer subclasse deles (Bound)
T_Num = TypeVar('T_Num', bound=float)

def duplicar(valor: T_Num) -> T_Num:
    return valor * 2

