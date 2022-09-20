colorActual = ['verde', 'amarillo', 'rojo']
def avanza_semaforo(colorActual):
    if colorActual == 'verde':
        print('amarillo')
    if colorActual == 'amarillo':
        print('rojo')
    if colorActual == 'rojo':
        print('verde')
    if colorActual != 'verde' or 'amarillo' or 'rojo':
        print('No es un color correcto')

avanza_semaforo('amarillo')


#print(next(colorActual))   
        
#  coleccion = {Alejandro: 22, Maria: 20, Sabrina: 31, Daniel:35}
# for i in coleccion:
#   print(f'{i} -> {coleccion[i]')
#   

# for clave, valor in coleccion.items(): #Items recorre todos los elementos del diccionario.
#   print(f'{clave} -> {valor})

#RECORRER CARACTERES
# coleccion = 'sabrina'
# for i in coleccion:
#   print('Hola mundo') #Me va a imprimir ocho veces que es la cantidad de caracteres de mi nombre, me va a escribir
# ocho veces 'Hola mundo'

#coleccion = 'sabrina'
# for i in coleccion:
#   print(f'{i}',end='.')