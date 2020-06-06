from src.bingo import carton
from src.bingo import llenas_consecutivas

def test_columnas_mayores():
    mi_carton = carton()
    assert llenas_consecutivas(mi_carton)
