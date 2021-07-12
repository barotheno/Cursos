"""
Nos permite repetir un bloque de codigo infinitamente mientras el resultado
sea True, en el momento que el resultado sea False, terminará el bucle.

"""

# While básico

# condicion = True

#while condicion:
#    print('Ejecutando ciclo while')
#else:
#    print('Fin del ciclo while')

# Ejemplo cambiando nuestra condición en algun momento

contador = 0
while contador < 1000:# Mientras contador sea menor que 3
    print(contador)
    contador += 1
else:
    print('Ciclo while fin')

