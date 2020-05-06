from src.bingo import carton
from src.bingo import mayores_derecha

def test_mayores_derecha():
    mi_carton = carton()
    assert mayores_derecha(mi_carton)
