class MiClase:

    variables_clase = 'valor variable clase'
    def __init__(self, variable_instancia):
        self.variable_instancia = variable_instancia

    # Definir un metodo de clase

    @classmethod
    def metodo_clase(cls):
        # Indicando "cls" podremos acceder a las variables de clase
        print(cls.variables_clase)

MiClase.metodo_clase()
