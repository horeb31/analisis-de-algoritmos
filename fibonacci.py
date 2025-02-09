def papifibonacci(primer, segundo, limite, suma=0):
    if primer >= limite:  # Caso base
        print("\nSuma total:", suma)  # Imprimir la suma al final
        return

    print(primer, end=" ")  # Imprimir el número actual
    papifibonacci(segundo, primer + segundo, limite, suma + primer)  # Llamada recursiva

papifibonacci(0,1,0,20)

