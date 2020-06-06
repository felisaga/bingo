from src.bingo import carton
from src.bingo import cinco_celdas

def test_columnas_mayores():
    mi_carton = carton()
    assert cinco_celdas(mi_carton)
