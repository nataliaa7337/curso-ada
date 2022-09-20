def obtener_menor(numeros):
    contador = numeros[0]
    for elemento in numeros:
        if contador > elemento:
            contador = elemento
    return contador
obtener_menor([2, 6, 8, 20, 40, 12, 1, 4])

'''
def menor(lista):
    min = lista[0]
    for x in lista:
        if x < min:
            min = x
    return min
''''''