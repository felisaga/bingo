from src.bingo import carton

def test_contar_celdas_ocupadas():
    mi_carton = carton()
    contador = 0
    for fila in mi_carton:
        for celda in fila:
            contador = contador + celda

    # Esperamos encontrar 15 celdas ocupadas.
    assert contador == 15

#no tiene que haber menos de 15 celdas ocupadas
def test_menos_de_15():
    mi_carton = carton()
    contador = 0
    for fila in mi_carton:
        for celda in fila:
            contador = contador + celda
    assert contador > 14

#no tiene que haber mas de 15 celdas ocupadas
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
                columnas[contador] = 1 #si encuentro un 1 se que la columna esta ocupada
            contador += 1
    assert columnas == [1,1,1,1,1,1,1,1,1] #los 9 1 indican que todas las columnas tienen por lo menos una celda ocupada
