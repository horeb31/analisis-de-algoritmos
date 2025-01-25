"""
° Alexis González Reynoso
° Jair horeb Jiménez García
° Eliezer Mora González
"""


def CrearLista():# definir la función para crear el arreglo
    tamaño = int(input("Cuántos números va a querer rey? ")) # pedir el tamaño del arreglo
    arreglo = [] # crear el arreglo flaco, flaco
    for i in range(tamaño):
        arreglo.append(int(input(f"Ingresa los números {i}: "))) # pedir los números y agregarlos al arreglo con fstring para que se vea bonito
    return arreglo # retornar el arreglo

def ImprimirLista(arreglo): # definir la función para ver el arreglo
    for num in arreglo:
        print(num)

def QuickSort(arreglo,izquierdo,derecho): # definir la función para el quicksort
    # declarar las variables de las partes para dividir el arreglo
    i = izquierdo
    j = derecho
    mitad = arreglo[(izquierdo + derecho) // 2] # calcular la mitad del arreglo para poder agarrar el pivote
    while i <= j: # while para encontrar el pivote
        while arreglo[i] < mitad: # while para encontrar el pivote izquierdo del arreglo dividido
            i += 1
        while mitad < arreglo[j]: # while para encontrar el pivote derecho del arreglo dividido
            j -= 1
        if i <= j: # caso en el que el pivote izquierdo sea menor o igual al pivote derecho
            arreglo[i], arreglo[j] = arreglo[j], arreglo[i] # intercambiar los valores sin sobrescribirlos que sí no da errorq
            i += 1
            j -= 1
    if izquierdo < j: # caso en el que el pivote izquierdo sea menor que el pivote derecho
        QuickSort(lista, izquierdo, j) # llamar a la recursividad para dividir el arreglo en la parte izquierda del pivote
    if i < derecho:
        QuickSort(lista, i, derecho) # lo mismo, pero en la derecha

# éste bloque funciona como el main
lista = CrearLista()
QuickSort(lista, 0, len(lista)-1)
ImprimirLista(lista)


