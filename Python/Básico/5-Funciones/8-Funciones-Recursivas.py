# Es una funcion que se llama a si misma para completar una cierta tarea
# Realizaceros una función que averigüe el factorial de 5
"""
    5! = 5 * 4 * 3 * 2 * 1
    5! = 5 * 4 * 3 * 2
    5! = 5 * 4 * 6
    5! = 5 * 24
    5! = 120


"""

def factorial(numero):
    if numero == 1:
        return 1
    else:
        return numero * factorial(numero-1)

resultado = factorial(3)

print(f'El factorial es: {resultado}')