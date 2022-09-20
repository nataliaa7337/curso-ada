numeros = [0, 3, 5, 88, 10, 44, 103]
def contiene(numero, numeros):
    for elemento in numeros:
        if numero == elemento:
            return True
    
    return False        
contiene(103, numeros)



