def jugar_piedra_papel_tijera(a, b):
    if a and b == 'tijera' and 'piedra':
        print('Gano piedra!')
    elif a and b == 'piedra' and 'tijera':
        print('Gano piedra!')
    elif a and b == 'papel' and 'piedra':
        print('Gano papel!')
    elif a and b == 'piedra' and 'papel':
        print('Gano papel!')
    elif a and b == 'papel' and 'tijera':
        print('Gano tijera!')
    elif a and b == 'tijera' and 'papel':
        print('Gano tijera')
    elif a and b == 'piedra' and 'piedra':
        print('Empate!')
    elif a and b == 'papel' and 'papel':
        print('Empate!')
    elif a and b == 'tijera' and 'tijera':
        print('Empate!')
jugar_piedra_papel_tijera('papel','papel')


# SIIIIIII.
# me salio, gracias profe por decirme que iba elif, xq si pongo if en todo se tienen que cumplir todas las condiciones.