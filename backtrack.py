"""
° Alexis González Reynoso
° Jair horeb Jiménez García
° Eliezer Mora González
"""
def es_seguro(tablero, fila, col):
    # Verificar la columna
    for i in range(fila):
        if tablero[i] == col:
            return False

    # Verificar la diagonal superior izquierda
    for i, j in zip(range(fila, -1, -1), range(col, -1, -1)):
        if tablero[i] == j:
            return False

    # Verificar la diagonal superior derecha
    for i, j in zip(range(fila, -1, -1), range(col, len(tablero))):
        if tablero[i] == j:
            return False

    return True

def resolver_8_reinas(tablero, fila):
    if fila >= len(tablero): # Si hemos llenado todas las filas, hemos encontrado una solución
        return True

    for col in range(len(tablero)): # Buscamos una columna donde pueda colocar la reina
        if es_seguro(tablero, fila, col): # Si la columna es segura, colocamos la reina
            tablero[fila] = col
            if resolver_8_reinas(tablero, fila + 1):
                return True
            tablero[fila] = -1 # Si no encontramos una solución, borramos la reina

    return False

def imprimir_tablero(tablero): # Pues imprimir el tablero pa
    for fila in range(len(tablero)):
        linea = ""
        for col in range(len(tablero)):
            if tablero[fila] == col:
                linea += "Q "
            else:
                linea += ". "
        print(linea)
    print("\n")


tablero = [-1] * 8
if resolver_8_reinas(tablero, 0):
    imprimir_tablero(tablero)
else:
    print("No se encontró solución.")


