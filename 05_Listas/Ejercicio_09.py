tablero = [["-","-","-"], ["-","-","-"], ["-","-","-"]]
condicion = True
turno = "X"
jugadas = 0

print("BIENVENIDO AL JUEGO DE TA-TE-TI")

while condicion :
    print(f"-- Turno del jugador {turno} --")

    casilla_libre = False
    while not casilla_libre :
        fila_seleccionada = int(input("Ingrese la fila (0 a 2): "))
        columna_seleccionada = int(input("Ingrese la columna (0 a 2): "))

        if tablero[fila_seleccionada][columna_seleccionada] == "-" :
            casilla_libre = True
        else :
            print("-- Esa casilla ya está ocupada, elegí otra --")

    tablero[fila_seleccionada][columna_seleccionada] = turno
    jugadas += 1

    for fila in tablero :
        for columna in fila :
            print(columna, end=" ")
        print()

    ganador = False

    for fila in tablero :
        if fila[0] == fila[1] == fila[2] != "-" :
            ganador = True

    for columna in range(3) :
        if tablero[0][columna] == tablero[1][columna] == tablero[2][columna] != "-" :
            ganador = True

    if tablero[0][0] == tablero[1][1] == tablero[2][2] != "-" :
        ganador = True

    if tablero[0][2] == tablero[1][1] == tablero[2][0] != "-" :
        ganador = True

    if ganador :
        print(f"-- ¡Ganó el jugador {turno}! --")
        condicion = False
    elif jugadas == 9 :
        print("-- Empate, se llenó el tablero --")
        condicion = False
    else :
        if turno == "X" :
            turno = "O"
        else :
            turno = "X"
