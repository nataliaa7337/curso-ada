def obtener_sensacion(temperatura):
    if temperatura <0:
        print('Esta helado')
    if temperatura >= 0 and temperatura <15:
        print('Hace frio')
    if temperatura >=15 and temperatura <25:
        print('Esta lindo')
    if temperatura >= 25 and temperatura <30:
        print('Hace calor')
    if temperatura >= 30:
        print('Hace mucho calor!')
obtener_sensacion(-2)
obtener_sensacion(0)
obtener_sensacion(25)
obtener_sensacion(16)

