"""
En los diccionarios, primero tenemos un kei o id ( también llamado llave ) y a continuación el valor.  

"""
diccionario = {
    'Usuario': 'Ruben',
    'Juego': 'FortNite'
}
print(diccionario)
# Para saver el largo
print(len(diccionario))
# Acceder a un elemento (key)
print(diccionario['Usuario'])
# Otra forma de recuperar un elemento
print(diccionario.get('Juego'))
# Modificando elementos
diccionario['Juego'] = 'Call of dutty' 
# Recorrer los elementos de un diccionario

for termino in diccionario:
    print(termino)

print("")

# Para recorrer también los valores:

for termino1, valor in diccionario.items():
    print(termino1, valor)

# Para solo recuperar las llaves existe otra forma
print("")
for termino2 in diccionario.keys():
    print(termino2)

# Para solo recorrer los valores
print("")
for termino3 in diccionario.values():
    print(termino3)

# Comprobar si ya existe un elemento
print('Juegos' in diccionario)

# Agregar un elemento
diccionario['RTX'] = '3090'

# Remover elemento
diccionario.pop('Juego')

# Limpiar diccionario
diccionario.clear()

# Para elemininar por completo, incluido la variable

del diccionario