# Una lista, es un conjunto de elementos
"""
        nombreLista     0="Juan"    1="Roberto"     2="Pepe"
"""

# Creamos una lista

nombres = ['Juan', 'Karla', 'Ricardo', 'Maria']
# Imprimimos la lista de nombres
print(nombres)

# Acceder a los elementos de una lista
print(nombres[0])
print(nombres[1])

# Acceder a los elementos de manera inversa
print(nombres[-1])
print(nombres[-2])

# Imprimir un rango
print(nombres[0:2]) # Sin incluir el indice 2

# Ir del inicio de la lista al indice (sin incluirlo)
print(nombres[:3])

# Desde el indice indicado hasta el final de la lista
print(nombres[1:])

# Cambiar un valor de la lista
nombres[3] = 'Ivone'
print(nombres)

# Iterar una lista
for nombre in nombres:
    print(nombre)
else:
    print('No existen mas nombres en la lista')

# Preguntar cuantos elementos tiene
print(len(nombres))

# Agregar un elemento
nombres.append('Lorenzo')
print(nombres)

# Insertar un elementos en un indice especifico
nombres.insert(1, 'Octavio')
print(nombres)

# Remover un elemento
nombres.remove('Octavio')
print(nombres)

# Remover ultimo valor agregado
nombres.pop()
print(nombres)

# Eliminar un indice
del nombres[0]
print(nombres)

# limpiar la lista
nombres.clear()
print(nombres)

# Borrar la lista por completo
del nombres
print(nombres)
