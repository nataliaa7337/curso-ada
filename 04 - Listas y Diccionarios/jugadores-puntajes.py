jugadorA = 'Melisa'
jugadorB = 'Noe'

puntajesA = [3, 7, 5]
puntajesB = [10, 0, 5]

def obtener_resultado(jugadorA, jugadorB, puntajesA, puntajesB):
    sumaJugadorA = 0
    sumaJugadorB = 0
    for num in puntajesA:
        sumaJugadorA = sumaJugadorA + num
    for num in puntajesB:
        sumaJugadorB = sumaJugadorB + num
        
    if sumaJugadorA > sumaJugadorB:
        return 'Gana jugadorA' + jugadorA
    elif sumaJugadorB > sumaJugadorA:
        return 'Gana jugadorB' + jugadorB
    else:
        return 'Empate'    

obtener_resultado(jugadorA, jugadorB, puntajesA, puntajesB)
#EMPATE!

#CASO 2 del mismo ejercicio pero con otro jugadorC y puntajesC

jugadorA = 'Melisa'
jugadorB = 'Noe'
jugadorC = 'Daniel'

puntajesA = [3, 7, 5]
puntajesB = [10, 0, 5]
puntajesC = [8, 0, 2]



def obtener_resultado(jugadorA, jugadorB, jugadorC, puntajesA, puntajesB, puntajesC):
    sumaJugadorA = 0
    sumaJugadorB = 0
    sumaJugadorC = 0
    for num in puntajesA:
        sumaJugadorA = sumaJugadorA + num
    for num in puntajesB:
        sumaJugadorB = sumaJugadorB + num
    for num in puntajesC:
        sumaJugadorC = sumaJugadorC + num
        
    if sumaJugadorA > sumaJugadorB and sumaJugadorA > sumaJugadorC:
        return 'Gana jugadorA' + jugadorA
    elif sumaJugadorB > sumaJugadorA and sumaJugadorB > sumaJugadorC:
        return 'Gana jugadorB' + jugadorB
    elif sumaJugadorC > sumaJugadorA and sumaJugadorC > sumaJugadorB:
        return 'Gana jugadorC'
    else:
        return 'Empate'    

obtener_resultado(jugadorA, jugadorB,jugadorC, puntajesA, puntajesB, puntajesC)

