def obtener_nota(puntaje):
    if puntaje <6:
        print('Desaprobado')
    if puntaje >= 6 and puntaje <7:
        print('Regular')
    if puntaje >=7 and puntaje <8:
        print('Bueno')
    if puntaje >=8 and puntaje <10:
        print('Muy bueno')
    if puntaje == 10:
        print('Excelente')
    if puntaje <0 or puntaje >10:
        print('Puntaje invalido')
obtener_nota(10)

