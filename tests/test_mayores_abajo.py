from src.bingo import carton
from src.bingo import mayores_abajo

def test_mayores_abajo():
    mi_carton = carton()
    assert mayores_abajo(mi_carton)
