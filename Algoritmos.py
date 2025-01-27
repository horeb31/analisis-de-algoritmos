"""
° Alexis González Reynoso
° Jair horeb Jiménez García
° Eliezer Mora González
"""

# definir la función para crear el arreglo
def CrearLista():
    tamaño = int(input("Cuántos números va a querer rey? ")) # pedir el tamaño del arreglo
    arreglo = [] # crear el arreglo flaco, flaco
    for i in range(tamaño):
        arreglo.append(int(input(f"Ingresa los números {i}: "))) # pedir los números y agregarlos al arreglo con fstring para que se vea bonito
    return arreglo # retornar el arreglo

def PedirBúsqueda():
    búsqueda = int(input("Ingresa el número para buscar al perdido: "))
    return búsqueda

# definir la función para ver el arreglo
def ImprimirLista(arreglo): 
    for num in arreglo:
        print(num)

# definir la función para el quicksort
def QuickSort(arreglo,izquierdo,derecho): 
    # declarar las variables de las partes para dividir el arreglo
    i = izquierdo
    j = derecho
    pivote = arreglo[(izquierdo + derecho) // 2] # calcular la pivote del arreglo para poder agarrar el pivote
    while i <= j: # while para encontrar el pivote
        while arreglo[i] < pivote: # while para encontrar el pivote izquierdo del arreglo dividido
            i += 1
        while pivote < arreglo[j]: # while para encontrar el pivote derecho del arreglo dividido
            j -= 1
        if i <= j: # caso en el que el pivote izquierdo sea menor o igual al pivote derecho
            arreglo[i], arreglo[j] = arreglo[j], arreglo[i] # intercambiar los valores sin sobrescribirlos que sí no da errore
            i += 1
            j -= 1
    if izquierdo < j: # caso en el que el pivote izquierdo sea menor que el pivote derecho
        QuickSort(lista, izquierdo, j) # llamar a la recursividad para dividir el arreglo en la parte izquierda del pivote
    if i < derecho:
        QuickSort(lista, i, derecho) # lo mismo, pero en la derecha

# definir el algoritmo de búsqueda binaria
def BúsquedaBinaria(arreglo, izquierdo, derecho, búsqueda):
    if izquierdo > derecho:  # caso base en que pues no se encuentre el elemento
        return 0 

    pivote = (izquierdo + derecho) // 2  # calcular el índice del pivote

    if arreglo[pivote] == búsqueda:  # se encontró el número
        return pivote  
    # llamada recursiva para hacer todo el pedo del divide y vencerás
    elif arreglo[pivote] < búsqueda:  
        return BúsquedaBinaria(arreglo, pivote + 1, derecho, búsqueda)
    else:  
        return BúsquedaBinaria(arreglo, izquierdo, pivote - 1, búsqueda)


# éste bloque funciona como el main
lista = CrearLista()
# sí la lista está vacía
if len(lista) == 0:  
    print("La lista está vacía pa")
# sí se creó la lista bien
else:
    QuickSort(lista, 0, len(lista) - 1)
    ImprimirLista(lista)

    if len(lista) == 1:
        print("La lista tiene un solo elemento, no hay necesidad de buscar, está en el índice 0")
    else:
        búsqueda = PedirBúsqueda()
        resultado = BúsquedaBinaria(lista, 0, len(lista) - 1, búsqueda)
        
        if resultado != -1:  # Ajuste: -1 se devuelve cuando no se encuentra
            print(f"El número {búsqueda} fue encontrado en el índice {resultado}.")
        else:
            print(f"El número {búsqueda} no está en la lista.")





