# En una tupla no se pueden modificar, agregar o eliminar elementos

# Definir una tupla

frutas = ('Naranja', 'Platano', 'Guayaba')
print(frutas)

# Saber el largo de una tupla
print(len(frutas))

# Acceder a un elemento
print(frutas[0])

# Navegacion inversa
print(frutas[-1])

# Acceder a un rango
print(frutas[0:1])# Sin incluir el último indice

# Recorrer elementos de una tupla
for fruta in frutas:
    print(fruta)
else:
    print("No quedan mas frutas")

# Si en el ciclo for, no queremos que haga el salto de linea por defecto un itilizamos el parámetro "END"

for fruta in frutas:
    print(fruta, end=' ')

# Cambiar de tupla a lista

frutaLista = list(frutas)

# Cambiar de lista a tupla

frutas = tuple(frutaLista)