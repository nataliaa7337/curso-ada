cantid_cuadros = int(input('Ingrese cantidad de cuadros'))
tiempo_actual = 80 #minutos
tiempo_inicial = 20 #minutos
tiempo = tiempo_actual + tiempo_inicial

def calcular_fps(cantid_cuadros, tiempo):
    return cantid_cuadros / tiempo
calcular_fps(cantid_cuadros, tiempo)

    
#fps = cn / (tiempo_actual - tiempo_inicial)
#Fuente: https://www.iteramos.com/pregunta/18020/calcular-los-fotogramas-por-segundo-en-un-juego