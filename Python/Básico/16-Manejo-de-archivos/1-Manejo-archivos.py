'''
Podemos manejar archivos de texto TXT
Podemos manejar archivos binarios, fotos, audios, videos etc.

Aqui veremos como trabajar con archivos tipo TXT
'''
# Con open podremos abrir un archivo ya existente, o crear un archivo nuevo.
# En este caso crearemos un archivo nuevo llamado 'prueba.txt'
# Por si surgen errores, atraparemos el codigo con un try
try:
    archivo = open('prueba.txt', 'w', encoding='utf8')# 'w' significa que indicamos que queremos escribir en el
    # Para escribir dentro de el archivo hacemos lo siguiente:
    archivo.write('Agregamos información al archivo\n')#Salto de linea \n
    archivo.write('Adios')
except Exception as e:
    print(e)
finally:
    archivo.close()#Indicamos que el archivo debe cerrarse con errores o sin ellos.
    print('Fin del archivo')
