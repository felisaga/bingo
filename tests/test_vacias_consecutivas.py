from src.bingo import carton
from src.bingo import vacias_consecutivas

def test_columnas_mayores():
    mi_carton = carton()
    assert vacias_consecutivas(mi_carton)
