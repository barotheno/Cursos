"""
Nos permite seleccionar un camino u otro

"""

condicion = True 

# Básica, if ( si es verdadera ) y si no es verdadera entonces ejecuta else

if condicion:
    print('Condicion verdaderas')
else:
    print('Condicion falsa')

# En esta ocasion si nonguna de las dos condiciones existe, entonces ejecutamos else

if condicion == True:
    print('Condicion verdadera')
elif condicion == False:
    print('Condicion falsa')
else:
    print('Condicion no reconocida')