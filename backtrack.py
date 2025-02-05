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
    if fila >= len(tablero):
        return True

    for col in range(len(tablero)):
        if es_seguro(tablero, fila, col):
            tablero[fila] = col
            if resolver_8_reinas(tablero, fila + 1):
                return True
            tablero[fila] = -1

    return False

def imprimir_tablero(tablero):
    for fila in range(len(tablero)):
        linea = ""
        for col in range(len(tablero)):
            if tablero[fila] == col:
                linea += "Q "
            else:
                linea += ". "
        print(linea)
    print("\n")

def main():
    tablero = [-1] * 8
    if resolver_8_reinas(tablero, 0):
        imprimir_tablero(tablero)
    else:
        print("No se encontró solución.")

if __name__ == "__main__":
    main()
