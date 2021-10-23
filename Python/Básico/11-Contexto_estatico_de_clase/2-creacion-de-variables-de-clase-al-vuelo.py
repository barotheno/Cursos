class MiClase:

    variables_clase = 'valor variable clase'
    # Aqui tenemos la variable de clase
    def __init__(self, variable_instancia):
        # Por este lado tenemos nuestra variable de instancia, anteriormente explicada
        self.variable_instancia = variable_instancia

# Para acceder a la variable de clase sin crear un objeto:

print(MiClase.variables_clase)
miClase = MiClase('Valor variable instancia')

# Podemos definir una nueva variable de clase directamente así:

MiClase.variable_clase2 = 'Valor variable clase 2'
