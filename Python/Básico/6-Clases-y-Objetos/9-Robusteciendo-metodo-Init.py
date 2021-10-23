class Persona:
    # Para pasar como argumentos una tupla: *args | Para un diccionario: **kwargs | Tambien podemos cambiar el nombre a nuestro gusto
    def __init__(self, nombre, apellido, edad, *valores, **terminos):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.valores = valores
        self.terminos = terminos

    # Definición de un método ( Función )

    def mostrar_detalle(self):  # Se agrega siempre el metodo de instancia "self"
        print(f'Persona: {self.nombre} {self.apellido} {self.edad} {self.valores} {self.terminos}')


# De esta forma podremos seguir pasando valores tipo tupla o diccionario:

persona1 = Persona('Ruben', 'Pedroche', 34, '695949939', 2, 3, 5, m='manzana', p='pera')
# Llamar método
persona1.mostrar_detalle()
