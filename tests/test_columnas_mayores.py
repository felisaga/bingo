from src.bingo import carton
from src.bingo import columnas_decenas

def test_columnas_mayores():
    mi_carton = carton()
    assert columnas_decenas(mi_carton)
