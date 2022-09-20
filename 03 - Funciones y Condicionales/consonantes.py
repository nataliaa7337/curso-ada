vocal = ['a', 'e', 'i', 'o', 'u']
miabecedarioconsonante = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'ñ', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
def es_consonante(letra):
    if letra in miabecedarioconsonante == miabecedarioconsonante:
        print(f'{letra} es una consonante')
    elif letra in vocal == vocal:
        print(f'{letra} es una vocal')
    else:
        print('No ha introducido una letra')
es_consonante('e')
es_consonante('j')

