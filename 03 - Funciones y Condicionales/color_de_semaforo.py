def puede_avanzar(color_semaforo):
    if color_semaforo == 'verde':
        print('Puede pasar')
    elif color_semaforo == 'rojo' or 'amarillo':
        print('No puede pasar')
    else:
        print('Error: color de semáforo inválido')
puede_avanzar('verde')