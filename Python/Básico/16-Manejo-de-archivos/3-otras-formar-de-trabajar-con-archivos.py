archivo = open('prueba.txt', 'r', encoding='utf8')

# Iterar el archivo

for linea in archivo:
    print(linea)

# leer lineas

print(archivo.readlines())

# Acceder a una linea de la lista
print(archivo.readlines())

# abrimos un  nuevo archivo
# a - anexar informacion
archivo2 = open('copia.txt', 'a')
archivo2.write(archivo.read())

archivo.close()
archivo2.close()
print('Se termino el proceso de leer y copiar')