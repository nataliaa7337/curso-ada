calle = input ('Ingrese su nombre de calle')
numero_de_calle = int ( input ('Ingrese su numero de calle'))
departamento = input ('Ingrese su departamento')
cod_postal = int (input('Ingrese su codigo postal'))
ciudad = input ('Ingrese su ciudad')
pais = input ('Ingrese su pais')
mensaje = 'La direccion que ha ingresado es:'
print('{6}, {0}, {1}, {2}, {3}, {4}, {5}'.format(calle, numero_de_calle, departamento, cod_postal, ciudad, pais, mensaje))