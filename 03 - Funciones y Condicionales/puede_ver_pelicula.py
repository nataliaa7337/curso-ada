edad = int (input('Ingrese su edad'))
tiene_autorizacion = int(input('Si tiene autorizacion, ingrese 1 sino 0'))

def puede_ver_pelicula(edad, tiene_autorizacion):
    if edad >= 15 or tiene_autorizacion == 1:
        return True and 'Puede ver pelicula'
    else:
        return False and 'No puede ver pelicula'
puede_ver_pelicula(edad, tiene_autorizacion)
puede_ver = puede_ver_pelicula(edad, tiene_autorizacion)
print(puede_ver)

# INGRESAMOS LA EDAD, INGRESA EL USER SI TIENE AUTORIZACION, LUEGO DEFINIMOS LA FUNCION PUEDE VER PELICULA
# LUEGO SI ES MAYOR O IGUAL A QUINCE SU EDAD O SI TIENE AUTORIZACION, RETORNA TRUE Y PUEDE VER PELICULA SINO
#DEVUELVE FALSE, NO PUEDE VER PELICULA.
''''''

