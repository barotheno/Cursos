# Las variables de clases, se asociaran directamente con la clase en si misma y no con los objetos, de esta manera cuando declaremos una
# variable de clase esta variable se compartirá con todos los objetos, por lo tanto en todos los objetos tendrá la misma información.

class MiClase:

    variables_clase = 'valor variable clase'
    # Aqui tenemos la variable de clase
    def __init__(self, variable_instancia):
        # Por este lado tenemos nuestra variable de instancia, anteriormente explicada
        self.variable_instancia = variable_instancia

# Para acceder a la variable de clase sin crear un objeto:

print(MiClase.variables_clase)