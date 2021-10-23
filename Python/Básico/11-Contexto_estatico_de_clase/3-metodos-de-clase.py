# Así como tenemos variables de clase, también podemos tener métodos de clase.
# Tenemos dos tipos de metodos que se pueden asociar con una clase, por un lado
#   Metodos estaticos
#   Metodos de clase

class MiClase:

    variables_clase = 'valor variable clase'
    
    def __init__(self, variable_instancia):
        self.variable_instancia = variable_instancia

    # METODOS ESTATICOS
    # Para indicar que un metodo es estatico, es decir que se asocia a la clase en si misma
    @staticmethod
    def metodo_estatico():#No recibe la variable de self
        # Los metodos estaticos no pueden acceder a las variables de instancia "self" pero si a las variables de clase
        print(MiClase.variables_clase)


MiClase.metodo_estatico()