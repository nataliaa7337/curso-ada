from asyncio.windows_events import NULL
import proceso_cuentas
import csv

def imprimir_cuentas(cuentas):
    for cuenta in cuentas:
        print("{} : {} : {}".format(
            cuenta[0],
            cuenta[1],
            cuenta[2]
        ))

def aplicar_gastos(cuentas, cuenta, monto):
    for c in cuentas:
        if c[0] == cuenta:
            total = float(c[2]) - monto
            if total < 0:
                print('Gasto todo el dinero, por favor recargar cuenta !!!!!\n'*3)
            c[2] = str(total)
            break
    return cuentas

def procesar_gastos(cuentas):
    archivo = open("gastos.csv")
    primera_linea = True
    for linea in archivo:
        if not primera_linea:
            nro_de_cuenta, importe_gasto = linea.replace('\n', '').split(',')
            importe_gasto_float = float(importe_gasto)
            cuentas_actualizadas = aplicar_gastos(cuentas, nro_de_cuenta, importe_gasto_float)
        else:
            primera_linea = False
    archivo.close()
    return cuentas_actualizadas

def aplicar_depositos(cuentas, nro_cuenta, deposito):
    for cuenta in cuentas:
        if cuenta[0] == nro_cuenta:
            cuenta[2] = str(float(cuenta[2]) + deposito)
            break
    return cuentas

def procesar_depositos(cuentas):
    archivo = open("depositos.csv")
    primera_linea = True
    for linea in archivo:
        if not primera_linea:
            nro_cuenta, monto_deposito = linea.replace('\n', '').split(',')
            importe_deposito_float = float(monto_deposito)
            cuentas_actualizadas = aplicar_depositos(cuentas, nro_cuenta, importe_deposito_float)
        else:
            primera_linea = False
    archivo.close()
    return cuentas_actualizadas

def actualizar_Cuentas(cuenta_origen, cuenta_Destino, cuentas):
    if cuenta_origen != [] and cuenta_Destino != []:
        for cuenta in cuentas:
            if cuenta[0] == cuenta_origen[0]:
                cuenta = cuenta_origen
            else:
                if cuenta[0] == cuenta_Destino[0]:
                    cuenta = cuenta_Destino
    return cuentas;

def aplicar_transferencias(cuentas, nro_de_cuenta_origen, nro_de_cuenta_destino, monto):
    cuenta_origen= []
    cuenta_Destino= []
    for cuenta in cuentas:
        if cuenta[0] == nro_de_cuenta_origen:
                cuenta_origen = cuenta
        else:
            if cuenta[0] == nro_de_cuenta_destino:
                cuenta_Destino = cuenta
    if cuenta_origen != [] and cuenta_Destino != []:
        if float(cuenta_origen[2]) > float(monto):
            cuenta_origen[2] = str(float(cuenta_origen[2]) - float(monto))
            cuenta_Destino[2] = str(float(cuenta_Destino[2]) + float(monto))   
    return actualizar_Cuentas(cuenta_origen, cuenta_Destino, cuentas)            


def transferencias(cuentas_actualizadas):
    cuentasAct = []
    archivo = open("transferencias.csv")
    primera_linea = True
    fileTransferencias = csv.reader(archivo)
    for nro_de_cuenta_origen,nro_de_cuenta_destino,monto in fileTransferencias:
        if primera_linea == True:
            primera_linea = False
        else:        
            cuentasAct = aplicar_transferencias(cuentas_actualizadas,nro_de_cuenta_origen,nro_de_cuenta_destino,monto)
    return cuentasAct           


def main():
    print('Obteniendo cuentas . . . ')
    cuentas = proceso_cuentas.obtener_cuentas()
    imprimir_cuentas(cuentas)

    print('Aplicando gastos . . . ')
    cuentas_actualizadas = procesar_gastos(cuentas)
    imprimir_cuentas(cuentas_actualizadas)

    print('Aplicando depositos . . .')
    cuentas_actualizadas_ = procesar_depositos(cuentas)
    imprimir_cuentas(cuentas_actualizadas_)
    
    print('Vamos a las Transferencias... ')
    cuentasAct = []
    cuentasAct = transferencias(cuentas_actualizadas_)
    if cuentasAct != []:
        imprimir_cuentas(cuentasAct)


if __name__ == '__main__':
    main()
    