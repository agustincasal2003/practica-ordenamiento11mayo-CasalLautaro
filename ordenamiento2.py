#Dada la siguiente lista: 34, 92, 100, 59, 87, 90, 1. Ordenar en orden descendente

def ordenar_descendente(lista)->int:
    numero = len(lista)
    for i in range(numero-1):
        for j in range(i+1, numero):
            if lista[i] < lista[j]:
                temporal = lista[i]
                lista[i] = lista[j]
                lista[j] = temporal
    return lista

valores = [34, 92, 100, 59, 87, 90, 1]
print("Orden descendente:", ordenar_descendente(valores))