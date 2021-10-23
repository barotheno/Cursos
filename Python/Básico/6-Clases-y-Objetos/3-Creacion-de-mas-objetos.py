# Agregamos parametros a nuestro método INIT

class Persona:
    def __init__(self, nombre, apellido, edad):# Agregamos parámetros
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

# Pasar parametros a nuevo objeto

persona1 = Persona('Ruben', 'Pedroche', 34)
print(persona1.nombre)

# Definimos un segundo objeto

persona2 = Persona('Carla', 'Gomez', 22)
print(f'Objeto Persona 2: {persona2.nombre} {persona2.apellido} {persona2.edad}')