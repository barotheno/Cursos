#La herencia es un proceso mediante el cual se puede crear una clase hija que hereda de una clase padre, compartiendo sus métodos y atributos. 
#Además de ello, una clase hija puede sobreescribir los métodos o atributos, o incluso definir unos nuevos.

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
# A continuacion creamos un objeto hijo de la clase padre Persona.

    def __str__(self):
        return f'Persona: {self.nombre} {self.edad}'

class Empleados(Persona):
    def __init__(self, nombre, edad, sueldo):
        super().__init__(nombre, edad)
        self.sueldo = sueldo

    def __str__(self):
        return f'{super().__str__()} {self.sueldo}'

if __name__ == '__main__':

    empleado1 = Empleados('Ruben', 28, 3000)
    print(empleado1.nombre)
    print(empleado1.edad)
    print(empleado1.sueldo)