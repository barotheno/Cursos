# Creamos una clase

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __add__(self, other):
        return f'{self.nombre} {other.nombre}'

    def __sub__(self, other):
        return self.edad - other.edad

persona1 = Persona('Juan', 87)
persona2 = Persona('Ruben', 34)
print(persona1 + persona2)
print(persona1 - persona2)