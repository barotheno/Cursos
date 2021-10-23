# Para definir una función con parámetro como diccionarios

def listaTerminos(**terminos):
    for llave, valor in terminos.items():
        print(f'{llave}: {valor}')

listaTerminos(IDE='IDEnviroment')