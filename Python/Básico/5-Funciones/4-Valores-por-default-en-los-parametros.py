# Para asignar un valor por defecto en una función:

def sumar (a = 0, b = 0):
    return a + b

# Ejemplos:

resultado = sumar()

print(f'Resultado default sumar: {resultado}')
print(f'Resultado introduciendo parametros: {sumar(38,45)}')

