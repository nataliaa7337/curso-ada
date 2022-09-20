filename = 'naty.txt'
print("Ingrese la frase a buscar en el archivo")
frase = input()

with open(filename) as f_obj:
    lines = f_obj.readlines()

large_str = ''
for line in lines:
 #   large_str += line.rstrip()
     if line.find(frase) != -1:
      print( line  )
# Contar las líneas
# print( lines )

# Accediendo al contenido por partes
#print( large_str[:14] + "..." )

#print( len( large_str ) )