hora = 'HH:mm'
def es_hora_valida(hora, minutos):
    if hora == 'HH:mm':
        return 'Hora valida'
    elif hora == '00:00' and minutos < 60:
        return 'Hora valida'
    elif hora < 25 and minutos >= 0:
        return 'Hora valida'
    else:
        return 'Formato invalido'
es_hora_valida(22:80)



'''       
time = "5:33 PM"
hour = datetime.strptime(time, '%H:%M %p').time()
'''