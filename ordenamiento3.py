#Buscar el valor de la lista anterior e indicar su posición. Eliminar el valor más grande.

def buscar_valor(lista, valor)->int:
    posicion = -1
    for i in range(len(lista)):
        if lista[i] == valor:
            posicion = i
    return posicion

def eliminar_mayor(lista)->int:
    mayor = lista[0]
    posicion_mayor = 0
    for i in range(1, len(lista)):
        if lista[i] > mayor:
            mayor = lista[i]
            posicion_mayor = i

    # desplazar elementos a la izquierda
    for i in range(posicion_mayor, len(lista)-1):
        lista[i] = lista[i+1]

    # nueva lista de tamaño reducido
    nueva = [0] * (len(lista)-1)
    for i in range(len(nueva)):
        nueva[i] = lista[i]
    return nueva

valores = [34, 92, 100, 59, 87, 90, 1]
print("Posición del 87:", buscar_valor(valores, 87))
print("Lista sin el mayor:", eliminar_mayor(valores))
