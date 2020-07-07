[![Build Status](https://travis-ci.com/felisaga/bingo.svg?branch=master)](https://travis-ci.com/felisaga/bingo) [![Coverage Status](https://coveralls.io/repos/github/felisaga/bingo/badge.svg?branch=master)](https://coveralls.io/github/felisaga/bingo?branch=master) [![Scrutinizer Code Quality](https://scrutinizer-ci.com/g/felisaga/bingo/badges/quality-score.png?b=master)](https://scrutinizer-ci.com/g/felisaga/bingo/?branch=master) (10)

# Bingo :white_haired_woman: :older_man: :partying_face::partying_face::partying_face::older_woman: :person_white_hair::manual_wheelchair::cowboy_hat_face:

Código en Python 3 que genera un cartón de bingo. Escrito para Adaptación Del Ambiente De Trabajo, Instituto Politécnico Superior "Gral. San Martín", 2020.


# Reglas

Se considara un cartón válido al que cumple con las siguientes condiciones:

    Cada carton es una matrix de 3 x 9.
    Los números del carton se encuentran en el rango 1 a 90.
    Cada columna de un carton (contando de izquierda a derecha) contiene numeros que van del 1 al 9, 10 al 19, 20 al 29 ..., 70 al 79 y 80 al 90.
    No hay números repetidos en el carton.
    Cada fila de un carton tiene exactamente 5 celdas ocupadas.
    Cada carton es una matrix de 3 x 9.
    Cada carton tiene 15 celdas ocupadas.
    Los números de las columnas izquierdas son menores que los de las columnas a la derecha.
    Para una misma columna, sus números están ordenados de menor a mayor de arriba hacia abajo.
    No pueden existir columnas vacias.
    No pueden existir columnas con sus tres celdas ocupadas.
    Cada carton debe tener 3 y solo 3 columas con solo una celda ocupada.
    En una fila no existen más de dos celdas vacías consecutivas.
    En una fila no existen más de dos celdas ocupadas consecutivas.
   
Para generar un carton escribir el siguiente comadno: :arrow_down:

python3 Juego.py

y para ver el carton en una pagina web escribir el comando " web/bingo_web.py " y se generara un archivo en la carpeta web que hay que abrir con un navegador

# Ejemplo de salida :ballot_box_with_check:


[0, 0, 20, 0, 47, 57, 0, 71, 89]

[0, 11, 26, 0, 49, 0, 0, 72, 90]

[9, 17, 0, 32, 0, 59, 63, 0, 0]
