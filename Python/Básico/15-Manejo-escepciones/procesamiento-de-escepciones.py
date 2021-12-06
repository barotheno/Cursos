
resultado = None
a = 10
b = 2

try:
    resultado = a/b
except Exception as e:
    print(f'Ocurrió un error: {e}')
#Podemos crear un else, en caso de que no se arrojen errores por ejemplo:
else:
    print('No hubo errores')
#Con el bloque finally, siempre ejecutaremos dicho bloque
finally:
    print('Soy el bloque finally')

print(f'Resultado: {resultado}')
print('Continuamos pues...')