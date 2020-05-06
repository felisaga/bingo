# Los 0 representan celdas vacias en el carton.
# Los 1 representan celdas ocupadas en el carton.
# <>
def carton():
    '''
    mi_carton = (
        (1,0,1,1,1,0,1,0,1),
        (0,1,0,1,0,1,1,0,1),
        (0,1,0,0,1,1,0,1,0)
    )
    '''
    mi_carton = (
        (0,11,0,32,44,0,62,73,0),
        (8,0,25,38,0,56,0,0,80),
        (0,17,29,0,47,0,67,0,88)
    )
    return mi_carton

def contar_celdas_ocupadas(carton):
    contador = 0
    for fila in carton:
        for celda in fila:
            if celda != 0:
                contador += 1
    return contador

def menos_de_15(carton):
    contador = 0
    for fila in carton:
        for celda in fila:
            if celda != 0:
                contador += 1
    return contador

def mas_de_15(carton):
    contador = 0
    for fila in carton:
        for celda in fila:
            if celda != 0:
                contador += 1
    return contador

columnas = [0,0,0,0,0,0,0,0,0]
def columnas_ocupadas(carton):
    for fila in carton:
        contador = 0
        for celda in fila:
            if celda != 0:
                columnas[contador] = 1 #si encuentro un 1 se que la columna esta ocupada
            contador += 1
    return columnas

def filas_vacias(mi_carton):
    for fila in mi_carton:
        x = 0
        for celda in fila:
            x += celda
        if x == 0:
            return False
    return True

def validar_numeros_carton(carton):
    for fila in carton:
        for celda in fila:
            if celda != 0 and (celda > 90 or celda < 0):
                return False
    return True
