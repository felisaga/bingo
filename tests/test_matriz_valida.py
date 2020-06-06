from src.bingo import carton
from src.bingo import matriz_valida

def test_columnas_mayores():
    mi_carton = carton()
    assert matriz_valida(mi_carton)
