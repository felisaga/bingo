
# Los 0 representan celdas vacias en el carton.
# Los 1 representan celdas ocupadas en el carton.
# <>

def carton():
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

def filas_vacias(carton):
    for fila in range(3):
        for fila in carton:
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

def mayores_derecha(carton):
    for fila in range(3):
        min = 0
        max = 10
        for columna in range(9):
            if carton[fila][columna] != 0:
                if (carton[fila][columna] < min or carton[fila][columna] > max):
                    return False
            min += 10
            max += 10
    return True

def mayores_abajo(carton):
    ban = 0
    for columna in range(9):
        for fila in range(3):
            if carton[fila][columna] != 0:
                if ban != 0:
                    if ban > carton[fila][columna]:
                        return False
                ban = carton[fila][columna]
        ban = 0
    return True

def nros_repetidos(carton):
    bandera = [0] * 100
    for fila in range(3):
        for columna in range(9):
            if carton[fila][columna] > 0 and carton[fila][columna] <= 90:
                if bandera[carton[fila][columna]] != 0:
                    return False
                bandera[carton[fila][columna]] = bandera[carton[fila][columna]] + 1
    return True

def columnas_decenas(carton):
    x = 0
    y = 9
    for columna in range(9):
        for fila in range(3):
            if carton[fila][columna] != 0:
                if not(x <= carton[fila][columna] <= y):
                    return False
        x += 10
        y += 10
        if y == 89:
            y = 90
    return True

def cinco_celdas(carton):
    for fila in carton:
        ban = 0
        for celda in fila:
            if celda != 0:
                ban += 1
        if ban != 5:
            return False
    return True

def matriz_valida(carton):
    filas = len(carton)
    for fila in range(3):
        columnas = 0
        columnas += len(carton[fila])
        if columnas != 9:
            return False
    return filas == 3 and columnas == 9

def columnas_vacias(carton):
    x = 0
    for columna in range(9):
        for fila in range(3):
            x += fila
        if x == 0:
            return False
    return True

def una_celda(carton):
    ban = 0
    for columnda in range(9):
        con = 0
        for fila in range(3):
            if carton[fila][columnda] != 0:
                con += 1
        if con == 1:
            ban += 1
    return ban == 3

def vacias_consecutivas(carton):
    for fila in range(3):
        for columna in range(7):
            if carton[fila][columna] == 0 and carton[fila][columna+1] == 0 and carton[fila][columna+2] == 0:
                return False
    return True
def llenas_consecutivas(carton):
    for fila in range(3):
        for columna in range(7):
            if carton[fila][columna] != 0 and carton[fila][columna+1] != 0 and carton[fila][columna+2] != 0:
                return False
    return True
