# Agregamos parametros a nuestro método INIT

class Persona:
    def __init__(self, nombre, apellido, edad):# Agregamos parámetros
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

# Pasar parametros a nuevo objeto

persona1 = Persona('Ruben', 'Pedroche', 34)
print(persona1.nombre)