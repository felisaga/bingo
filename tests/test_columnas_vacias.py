from src.bingo import carton
from src.bingo import columnas_vacias

def test_columnas_mayores():
    mi_carton = carton()
    assert columnas_vacias(mi_carton)
