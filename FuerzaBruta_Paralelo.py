"""
° Alexis González Reynoso
° Jair horeb Jiménez García
° Eliezer Mora González
"""

from multiprocessing import Process
import time

# Función para fuerza bruta
def doxeado (contraseña, diccionario):
    # Iniciar el reloj para saber cuanto tiempo se tardó en ser doxeado
    iniciar = time.perf_counter()

    # Hacer las comprobaciones
    for intento in diccionario:
        if intento == contraseña:
            print(f'Contraseña encontrada: {contraseña}')
            encontrado = True
            break
    else:
        print(f'Contraseña no encontrada: {contraseña}')
        encontrado = False

    # Terminar el conteo
    fin = time.perf_counter()
    # Mostrar el tiempo que se tardó en ser doxeado
    tiempo = fin - iniciar
    if encontrado == True:
        print("Se tardó ", tiempo, "segundos en valer camote") 
    else:
        print("Se tardó ", tiempo, "segundos, pero te salvaste mai")

# Main para programación paralela
def main():



    # Definir el diccionario de contraseñas
    contraseña1 = ['aguapapa','santorini','atlas','turuleca','contraseña']
    contraseña2 = ['barcelona','pepino','admin','pajarito','chocomilk']
    contraseña3 = ['de','blutu','divais','isconnected','suseksfoli']
    contraseña4 = ['alebrijes','jaguares','atlante','dorados', 'jaiba']
    # Pasar los argumentos como contraseña correcta
    proceso1 = Process(target= doxeado, args=('aguapapa', contraseña1,))
    proceso2 = Process(target= doxeado, args=('admin', contraseña2,))
    proceso3 = Process(target= doxeado, args=('divais', contraseña3,))
    proceso4 = Process(target= doxeado, args=('chuy mayaton', contraseña4,))

    proceso1.start()
    proceso2.start()
    proceso3.start()
    proceso4.start()

    proceso1.join()
    proceso2.join()
    proceso3.join()
    proceso4.join()


if __name__ == "__main__":
    main()