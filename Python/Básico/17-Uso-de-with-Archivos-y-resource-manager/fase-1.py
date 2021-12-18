'''
Como vimos anteriormente, para abrir un archivo utilizamos 'open()' y posteriormente cerramos
con close(). Si no lo cerramos python lo cerrara automaticamente, pero es recomendable hacerlo
nosotros.

Tambien lo recomendable es tenerlo en un bloque try y cerraro en 'finally'.

Sin embargo existe una sintaxis simplificada y de manera automatica que cerrará nuestro archivo y a esto se le conoce
como MANEJO DE CONTEXTO WITH

'''

#with open('prueba.txt','r', encoding='utf8') as archivo:
    # La ventaja de esto esque abre y cierra el archivo sin abrir bloque try y finally.
    #print(archivo.read())
    # with manda llamar dos metodos o clases __enter__ y __exit__
    # Pero tambien podemos crear nuestras propias clases como veremos a continuacion con 
    # nuestra clase 'manejo_archivos.py'

from ManejoArchivos import ManejoArchivos

with ManejoArchivos('prueba.txt') as archivo:
    print(archivo.read())