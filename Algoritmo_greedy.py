"""
° Alexis González Reynoso
° Jair horeb Jiménez García
° Eliezer Mora González
"""

def dar_cambio(monto):
    billetes_monedas = [1000, 500, 200, 100, 50, 20, 10, 5, 2, 1]  # Billetes y monedas 
    cambio = {} 
    
    for valor in billetes_monedas:
        if monto >= valor: # Si el monto es mayor o igual al valor de la moneda
            cantidad = monto // valor # Calcula la cantidad de monedas que se pueden entregar
            cambio[valor] = cantidad  # Agrega la moneda y su cantidad 
            monto -= cantidad * valor # Resta el valor de las monedas entregadas 
    
    return cambio

# Solicitar el monto al usuario
monto = int(input("Cuanto peso nenecitamos? "))
cambio = dar_cambio(monto)

print("Morralla dada:")
for valor, cantidad in cambio.items(): # Imprime el cambio
    tipo = "billete" if valor >= 20 else "moneda" # Determina si es un billete o moneda
    print(f"{cantidad} {tipo}(s) de ${valor} MXN") 