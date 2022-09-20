precios = {"manzana": 2, "naranja": 1.5, "platano": 4, "piña": 3}
while True:
    fruta = input("Dime la fruta que has vendido:")
    if fruta.lower() not in precios:
        print("Fruta no existe.")
    else:
        cantidad = int(input("Dime la cantidad de frutas que has vendido:"))
        print("El precio es de %f" % (cantidad * precios[fruta]))
    opcion = input("¿Quieres vender otra fruta (s/n)")
    while opcion.lower() != "s" and opcion.lower() != "n":
        opcion = input("¿Quieres vender otra fruta (s/n)")
    if opcion.lower() == "n":
        break



