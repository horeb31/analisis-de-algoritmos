"""
° Alexis González Reynoso
° Jair horeb Jiménez García
° Eliezer Mora González
"""


def papifibonacci(primer, segundo, limite, suma=0):
    # Caso base: si el número actual es mayor o igual al límite, finaliza.
    if primer >= limite:
        print("\nSuma total:", suma)
        return

    # Imprime el número actual y llama recursivamente con los siguientes valores.
    print(primer, end=" ")
    papifibonacci(segundo, primer + segundo, limite, suma + primer)

#llamamos la funcion con sus argumentos
papifibonacci(0, 1, 45)


