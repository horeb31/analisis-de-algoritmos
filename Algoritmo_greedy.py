"""
° Alexis González Reynoso
° Jair horeb Jiménez García
° Eliezer Mora González
"""

def dar_cambio(monto):
    billetes_monedas = [1000, 500, 200, 100, 50, 20, 10, 5, 2, 1]  # Billetes y monedas 
    cambio = {}
    
    for valor in billetes_monedas:
        if monto >= valor:
            cantidad = monto // valor
            cambio[valor] = cantidad
            monto -= cantidad * valor
    
    return cambio

# Solicitar el monto al usuario
monto = int(input("Cuanto peso nenecitamos? "))
cambio = dar_cambio(monto)

print("Morralla dada:")
for valor, cantidad in cambio.items():
    tipo = "billete" if valor >= 20 else "moneda"
    print(f"{cantidad} {tipo}(s) de ${valor} MXN")