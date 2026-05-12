#Se desea eliminar todos los números duplicados de una lista o vector (array).
#Por ejemplo, si el array toma los valores: 4 7 11 4 9 5 11 7 3 5 ha de cambiarse a
#4 7 11 9 5 3 Escribir una función que elimine los elementos duplicados de un array.



def eliminar_duplicados(lista)->int:
    """args: funcion eliminar dulicados enteros..
    
    la lista inicializa en 0 y multiplica por el tamaño de la lista

    """
    resultado = [0] * len(lista)
    indice_resultado = 0 

    for i in range(len(lista)):
        repetido = 0
        for j in range(indice_resultado):
            if lista[i] == resultado[j]:
                repetido = 1
        if repetido == 0:
            resultado[indice_resultado] = lista[i]
            indice_resultado += 1

    # recortO tamaño de la lista
    resultado_final = [0] * indice_resultado
    for i in range(indice_resultado):
        resultado_final[i] = resultado[i]
    return resultado_final

# Ejemplo de uso
original = [4, 7, 11, 4, 9, 5, 11, 7, 3, 5]
print("Sin duplicados:", eliminar_duplicados(original))
