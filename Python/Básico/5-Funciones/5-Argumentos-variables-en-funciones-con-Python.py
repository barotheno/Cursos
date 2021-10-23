# Como pasar argumentos variables a una funcion en python
# Definimos una función, iteramos una cantidad de nombres desconocida.

# Con el asterisco convertimos el parametro en una tupla


def listarNombres(*nombres):
    for nombre in nombres:
        print(nombre)

listarNombres('Juan','carla','Maria', 'Rubén')
