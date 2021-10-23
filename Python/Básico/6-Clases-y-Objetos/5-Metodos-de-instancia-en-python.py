# Un método es igual que una función. Pero se le llama método por que se asocia con una clase
class Persona:
    def __init__(self, nombre, apellido, edad):# Agregamos parámetros
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

    # Definición de un método ( Función )

    def mostrar_detalle(self):  # Se agrega siempre el metodo de instancia "self"
        print(f'Persona: {self.nombre} {self.apellido} {self.edad}')


# Pasar parametros a nuevo objeto

persona1 = Persona('Ruben', 'Pedroche', 34)
# Llamar método
persona1.mostrar_detalle()

# Definimos un segundo objeto

persona2 = Persona('Carla', 'Gomez', 22)
persona2.mostrar_detalle()