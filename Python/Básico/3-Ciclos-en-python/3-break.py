# Vamos a iterar en una cadena que contengan dos letras a

for letra in 'Holanda':
    if letra == 'a':
        print(f'Letra encontrada: {letra}')
        break #Rompe con el ciclo for, una ved que encontramos lo que queremos.
else:
    print('Fin del ciclo for')