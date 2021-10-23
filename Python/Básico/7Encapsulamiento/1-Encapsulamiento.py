# No es recomendable modificar un objeto


class Persona:
    # Para pasar como argumentos una tupla: *args | Para un diccionario: **kwargs | Tambien podemos cambiar el nombre a nuestro gusto
    def __init__(self, nombre, apellido, edad):
        self._nombre = nombre
        self.apellido = apellido
        self.edad = edad

    # Definición de un método ( Función )

    def mostrar_detalle(self):  # Se agrega siempre el metodo de instancia "self"
        print(f'Persona: {self.nombre} {self.apellido} {self.edad} {self.valores} {self.terminos}')


# De esta forma podremos seguir pasando valores tipo tupla o diccionario:

persona1 = Persona('Ruben', 'Pedroche', 34)
# Llamar método
persona1._nombre = 'Ana' # El guion bajo es un indicativo de que no se deberían modificar los valores
                         # Con doble guion bajo "__" Restringimos la modificacion de valor.
                         