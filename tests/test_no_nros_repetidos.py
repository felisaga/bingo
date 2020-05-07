from src.bingo import carton
from src.bingo import nros_repetidos

def test_nros_repetidos():
    mi_carton = carton()
    assert nros_repetidos(mi_carton)
