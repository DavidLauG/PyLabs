class citizen:
    citizenship = ""

    def __init__(self, name: str, city: str):
        
        self.name=name
        self.city = city

citizen.citizenship="Portugal"
p1=citizen("David","Lisbon")
p2=citizen("Laurindo","Porto")

#Todos cidadões com a mesma cidadania, mas cidades diferentes
print(f"Cidadania de cidadão 1 e 2, respectivamente: {p1.citizenship}, {p2.citizenship}") #Portugal
print(f"Naturalidade de cidadão 1: {p1.city}") #Lisbon
print(f"Naturalidade de cidadão 2: {p2.city}") #Porto

citizen.citizenship="Angola"
print(f"Cidadania de cidadão 1 e 2, respectivamente: {p1.citizenship}, {p2.citizenship}") #Portugal
print(f"Naturalidade de cidadão 1: {p1.city}") #Lisbon
print(f"Naturalidade de cidadão 2: {p2.city}") #Porto
p1.city="Luanda"
print(f"Naturalidade de cidadão 1 (actualizada): {p1.city}") #Luanda
print(f"Naturalidade de cidadão 2: {p2.city}") #Porto
p2.citizenship="Brasil"
print(f"Cidadania final de cidadão 1 e 2, respectivamente : {p1.citizenship}, {p2.citizenship}") #Brasil