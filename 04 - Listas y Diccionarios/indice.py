def obtener_indice(valor, lista):
    contador = 0
    for num in lista:
        if valor == num:
            return 'El numero esta en la lista' + valor + contador
        contador += 1
        
    return 'Ese numero no esta en la lista'
obtener_indice(1, [20, 4, 88, 60, 12, 1, 5, 9] )
obtener_indice(15, [20, 4, 88, 60, 12, 1, 5, 9] )
'''
Crear una función obtenerIndice que tome como argumento un 
valor cualquiera valor y una lista cualquiera lista y devuelva
el índice del primer ítem con dicho valor en la lista, o -1 si no hay ninguno.
'''