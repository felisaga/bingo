from src.bingo import carton
from src.bingo import una_celda

def test_columnas_mayores():
    mi_carton = carton()
    assert una_celda(mi_carton)
