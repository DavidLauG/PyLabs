import sys
import os

# Ajuste de path para alcançar as pastas raiz
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from container import TypedCollection, Displayable, Scorable
from src.lab04.models import SoftwareProduct, HardwareProduct

class CustomerReview:
    """Classe independente que atende ao protocolo Scorable por estrutura."""
    def __init__(self, product_name: str, stars: float) -> None:
        self.product_name = product_name
        self.stars = stars
    
    def score(self) -> float:
        return self.stars

def run_demo() -> None:
    print("=== LAB 06: GENERIC TYPING AND PROTOCOLS ===\n")

    # Instanciação da coleção tipada para Software
    software_catalog: TypedCollection[SoftwareProduct] = TypedCollection()
    
    software_catalog.add(SoftwareProduct("Windows 11", "Pro", 1500.0, 100, "ms.com", 5000))
    software_catalog.add(SoftwareProduct("Adobe Photoshop", "2024", 350.0, 50, "adobe.com", 2500))
    software_catalog.add(SoftwareProduct("PyCharm Pro", "2026", 0.0, 10, "jetbrains.com", 800))  # Produto Grátis

    # --- CENÁRIO 1: Demonstração dos Métodos FIND e FILTER (Nota 4) ---
    print("--- Сценарий 1: Строгий поиск и операции фильтрации ---")
    
    # Uso do FIND: Localizar o primeiro software gratuito (preço == 0)
    free_software = software_catalog.find(lambda p: p.price == 0)
    print(f"[FIND] Первое найденное свободное программное обеспечение: {free_software.name if free_software else 'Нет'}")

    # Uso do FILTER: Filtrar softwares que ocupam mais de 1000MB (1GB) de espaço
    heavy_software = software_catalog.filter(lambda p: p.file_size_mb > 1000)
    print(f"[FILTER] Обнаружено программное обеспечение размером более 1000 МБ ({len(heavy_software)}):")
    for sw in heavy_software:
        print(f"   -> {sw.name} ({sw.file_size_mb} MB)")

    # Uso do MAP: Extrair apenas as strings de download dos softwares
    links = software_catalog.map(lambda p: p.download_link)
    print(f"[MAP] Список ссылок, извлеченных из T -> R: {links}")

    # --- CENÁRIO 2: Protocolo Displayable (Nota 5 - Tipagem Estrutural) ---
    print("\n--- Сценарий 2: Отображаемый протокол (без прямого наследования) ---")
    
    # Injeção dinâmica para cumprir o contrato do Protocolo em tempo de execução
    SoftwareProduct.display = lambda self: f"[SOFTWARE] {self.name} | Version: {self.model}"
    HardwareProduct.display = lambda self: f"[HARDWARE] {self.name} | Stock: {self.stock}"

    display_collection: TypedCollection[Displayable] = TypedCollection()
    display_collection.add(software_catalog.get_all()[0])  # Windows 11
    display_collection.add(HardwareProduct("Server Dell", "R750", 45000.0, 5, 36))

    for item in display_collection.get_all():
        print(f"{item.display()}")

    # --- CENÁRIO 3: Protocolo Scorable (Nota 5 - Bound TypeVar) ---
    print("\n--- Сценарий 3: Протокол Scorable (классы без иерархических связей) ---")
    
    # Vinculamos uma regra de score aos produtos
    SoftwareProduct.score = lambda self: float(self.stock * 1.5)

    score_collection: TypedCollection[Scorable] = TypedCollection()
    score_collection.add(software_catalog.get_all()[0])  # Adobe Photoshop
    score_collection.add(CustomerReview("RGB Mechanical Keyboard", 4.9))  # Classe totalmente distinta

    for item in score_collection.get_all():
        print(f"Рассчитанный балл: {item.score()}")

if __name__ == "__main__":
    run_demo()
