valor = 10
minimo = 20
maximo = 30

def esta_en_rango(valor, minimo, maximo):
    if valor > minimo and  valor < maximo:
        return True
print(f'{valor} esta entre {minimo} y {maximo}')