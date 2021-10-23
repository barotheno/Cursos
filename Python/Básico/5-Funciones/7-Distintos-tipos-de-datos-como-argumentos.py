# Definimos una función que reciba una lista de elementos y que acceda a cada uno de sus elementos

def desplegarNombres(nombres):
    for nombre in nombres:
        print(nombre)

nombres = ['Juan', 'Karla', 'Guillermo']

desplegarNombres(nombres)