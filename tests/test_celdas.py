from src.bingo import carton

def test_contar_celdas_ocupadas():
    mi_carton = carton()
    contador = 0
    for fila in mi_carton:
        for celda in fila:
            contador = contador + celda

    # Esperamos encontrar 15 celdas ocupadas.
    assert contador == 15
def test_menos_de_15():
    mi_carton = carton()
    contador = 0
    for fila in mi_carton:
        for celda in fila:
            contador = contador + celda
    assert contador > 14

def test_mas_de_15():
    mi_carton = carton()
    contador = 0
    for fila in mi_carton:
        for celda in fila:
            contador = contador + celda
    assert contador < 16

columnas = [0,0,0,0,0,0,0,0,0]
def test_columnas_ocupadas():
    mi_carton = carton()
    for fila in mi_carton:
        contador = 0
        for celda in fila:
            if celda == 1:
                columnas[contador] = 1
            contador += 1
    assert columnas == [1,1,1,1,1,1,1,1,1]

def test_sin_filas_vacias():
    mi_carton = carton()
    for fila in mi_carton:
        x = 0
        for celda in fila: #si hay por lo menos un 1 ya va a dar bien el test
            x += celda
        assert x > 0
