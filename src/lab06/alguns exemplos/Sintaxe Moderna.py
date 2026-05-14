# Função genérica: aceita uma lista de qualquer tipo 'T' e retorna um item 'T'
def primeiro_elemento[T](lista: list[T]) -> T:
    return lista[0]

numeros = [1, 2, 3]
texto = ["A", "B", "C"]

# O validador estático infere automaticamente o tipo de retorno correto
num: int = primeiro_elemento(numeros)
txt: str = primeiro_elemento(texto)

print (num)
print (txt)
