from src.bingo import carton
from src.bingo import contar_celdas_ocupadas
from src.bingo import menos_de_15
from src.bingo import mas_de_15
from src.bingo import columnas_ocupadas
from src.bingo import filas_vacias

def test_contar_celdas_ocupadas():
    mi_carton = carton()
    # Esperamos encontrar 15 celdas ocupadas.
    assert contar_celdas_ocupadas(mi_carton) == 15

#no tiene que haber menos de 15 celdas ocupadas
def test_menos_de_15():
    mi_carton = carton()
    assert menos_de_15(mi_carton) > 14

#no tiene que haber mas de 15 celdas ocupadas
def test_mas_de_15():
    mi_carton = carton()
    assert mas_de_15(mi_carton) < 16

def test_columnas_ocupadas():
    mi_carton = carton()
    assert columnas_ocupadas(mi_carton) == [1,1,1,1,1,1,1,1,1] #los 9 1 indican que todas las columnas tienen por lo menos una celda ocupada

def test_sin_filas_vacias():
    mi_carton = carton()
    assert filas_vacias(mi_carton) > 0
