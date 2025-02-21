#Integrantes
"""
° Alexis González Reynoso
° Jair horeb Jiménez García
° Eliezer Mora González
"""

#Algoritmo Heurístico para el Problema de la Mochila
def heuristico(valores, pesos, capacidad):
    n = len(valores)
    ratios = [(valores[i] / pesos[i], i) for i in range(n)]
    ratios.sort(reverse=True)
    
    valor_total = 0
    peso_total = 0
    seleccionado_items = []
    
    for ratio, i in ratios:
        if peso_total + pesos[i] <= capacidad:
            seleccionado_items.append(i)
            valor_total += valores[i]
            peso_total += pesos[i]
    
    return valor_total, seleccionado_items


def prueba_heuristico():
    print("Test Mochila (Heurístico):")
    valores = [60, 100, 120]
    pesos = [10, 20, 21]
    capacidad = 50
    
    valor_total, seleccionado = heuristico(valores, pesos, capacidad)
    print(f"Valor total: {valor_total}")
    print(f"Items seleccionados: {seleccionado}")

  
if __name__ == "__main__":
    prueba_heuristico()
    