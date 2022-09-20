Ejercicios de procesamiento de archivos
1. Movimientos en cuenta virtual (en clase) Tenemos un archivo llamado cuentas.csv donde tenemos persistida la información de las cuentas actuales de nuestro micro-mini-banco virtual. También tenemos un archivo llamado gastos.csv donde tenemos los gastos de las cuentas del día de hoy. Se desea actualizar el saldo de cada una de las cuentas descontando los gastos, y volver a guardar la info actualizada en un archivo llamado cuentas_actualizadas.

cuentas.csv (crear el nuevo archivo con el siguiente contenido y nombrarlo cuentas.csv)

nro_de_cuenta, titular, saldo, activa
1000123,MERI IERVASI,12312.12,1
1000124,ANA VACIA,1.2,1
1000125,PEDRO LOPEZ,999,1
1000126,LEO MENDEZ,1000,1
1000127,AGUSTIN REY,100,1
1000128,AMELIA MENDEZ,78000,1

gastos.csv (crear el nuevo archivo con el siguiente contenido y nombrarlo gastos.csv)

nro_de_cuenta, monto
1000126,1000
1000127,50
1000123,2312.12
1000125,19
1000128,1.2
1000124,20

2. Conteos y Depositos (tarea) Extender la funcionalidad del programa del ejercicio 1, agregando el procesamiento del archivo depositos.csv donde tenemos los depositos del día. A las cuentas que tenemos en este archivo, agregarles el monto indicado.

Ademas:

Si la cuenta queda en negativo por los gastos, imprimir un mensaje de alerta
Si no existe la cuenta seguir procesando el archivo
Imprimir un mensaje con la cantidad de lineas procesadas en cada archivo (gastos.csv y depositos.csv)
depositos.csv (crear el nuevo archivo con el siguiente contenido y nombrarlo depositos.csv)

nro_de_cuenta, monto
1000126,1000
1000127,10000
1000125,8000
1000128,8000

3. Transferencias (tarea) Extender la funcionalidad del programa de los ejercicios 1 y 2 y agregar el procesamiento de un archivo llamado transferencias.csv

Tener en cuenta que:

Si el saldo en la cuenta origen no es suficiente, entonces NO hacer la transferencia (no sumar el saldo a la cuenta destino)
transferencias.csv (crear el nuevo archivo con el siguiente contenido y nombrarlo transferencias.csv)

nro_de_cuenta_origen, nro_de_cuenta_destino, monto
1000126,1000123,1001
1000127,1000124,500
1000125,1000127,800
1000128,1000129,800