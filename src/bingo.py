
import random
import math

def intento_carton():
    contador = 0

    carton = [
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0]
    ]
    numerosCarton = 0

    while numerosCarton < 15:
        contador += 1
        if contador == 50 :
            return intento_carton()
        numero = random.randint(1, 90)

        columna = math.floor(numero / 10)
        if columna == 9:
            columna = 8
        huecos = 0
        for i in range(3):
            if carton[i][columna] == 0:
                huecos += 1
            if carton[i][columna] == numero:
                huecos = 0
                break
        if(huecos < 2):
            continue

        fila = 0
        for j in range(3):
            huecos = 0
            for i in range(9):
                if carton[fila][i] == 0:
                    huecos += 1
            if huecos < 5 or carton[fila][columna] != 0:
                fila += 1
            else:
                break
        if fila == 3:
            continue

        carton[fila][columna] = numero
        numerosCarton += 1
        contador = 0

    for x in range(9):
        huecos = 0
        for y in range(3):
            if carton[y][x] == 0:
                huecos += 1
        if huecos == 3:
            return intento_carton()

    return carton

# Los 0 representan celdas vacias en el carton.
# Los 1 representan celdas ocupadas en el carton.
# <>

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

def columnas_ocupadas(carton):
    columnas = [0,0,0,0,0,0,0,0,0]
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
            if celda != 0 and (celda > 91 or celda < 0):
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

def carton ():
    while True:
        carton = intento_carton()
        if contar_celdas_ocupadas(carton) == 15 and columnas_ocupadas(carton) == [1,1,1,1,1,1,1,1,1] and filas_vacias(carton) and validar_numeros_carton(carton) and mayores_derecha(carton) and mayores_abajo(carton) and nros_repetidos(carton) and columnas_decenas(carton) and cinco_celdas(carton) and matriz_valida(carton) and columnas_vacias(carton) and una_celda(carton) and vacias_consecutivas(carton) and llenas_consecutivas(carton):
            break
    return carton

def imprimir(carton):
    for fila in carton:
        print(fila)
imprimir(carton())
