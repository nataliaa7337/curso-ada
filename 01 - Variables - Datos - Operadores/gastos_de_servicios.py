dinero_disponible = int(input("ingrese cuanto dinero tiene disponible : "))
servi1 =input("ingrese el nombre del servicio: ")
monto1 = int(input("ingrese el monto a pagar : "))
servicios_restantes = 2
saldo_restante = dinero_disponible - monto1 
print("te quedan servicios por pagar {} ".format(servicios_restantes))
print("quedan de saldo ${} disponible ".format(saldo_restante))

servi2 =input("ingrese el nombre del siguiente servicio: ")
monto2 = int(input("ingrese el monto a pagar : "))
servicios_restantes = 1
saldo_restante = dinero_disponible - monto1 - monto2
print("te quedan servicios por pagar {} ".format(servicios_restantes))
print("quedan de saldo ${} disponible ".format(saldo_restante))

servi3 =input("ingrese el nombre del siguiente servicio: ")
monto3 = int(input("ingrese el monto a pagar : "))
servicios_restantes = 0
saldo_restante = dinero_disponible - monto1 - monto2 - monto3
print("te quedan servicios por pagar {} ".format(servicios_restantes))
print("quedan de saldo ${} disponible ".format(saldo_restante))

print("el dinero total disponible fue de: $" ,dinero_disponible)
print("Pago por" ,servicio1, "$" ,monto1)
print("pago por" ,servicio2, "$" ,monto2)
print("pago por" ,servicio3, "$" ,monto3)
print("El dinero que le queda en su cuenta es de : $" ,saldo_restante)