'''
r = read = lectura
a = append = Anexar informacion a un archivo que ya contiene información
w = write
x = crear
t = tipo de texto a crear
b = tipo binario a crear
'''
try:
    archivo = open('prueba.txt', 'r', encoding='utf8')
    print(archivo.read())
except Exception as e:
    print(e)
finally:
    archivo.close()
    print('Archivo finalizado')