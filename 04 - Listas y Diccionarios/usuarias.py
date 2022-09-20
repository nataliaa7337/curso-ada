users = ['Ada', 'Sabrina', 'Noe', 'Virginia']

def obtener_chat_status(usuarias):
    counter = 0
    for personas in usuarias:
        counter += 1
        
    if counter == 0:
        return 'No hay nadie conectado'
    elif counter == 1:
        return 'nombre_usuaria_1 esta conectada'
    elif counter == 2:
        return 'nombre_usuaria_2 esta conectada'
    else:
        return 'NOMBRE_USUARIA_1, NOMBRE_USUARIA_2 y X persona(s) más están conectadas'
obtener_chat_status(users)


        
        
        








