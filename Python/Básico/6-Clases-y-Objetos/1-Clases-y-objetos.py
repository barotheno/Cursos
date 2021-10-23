# Una clase es una plantilla en la cual podremos crear instancias u objetos
# Una clase puede contener atributos o métodos

# Crear una clase:

class Personas:
    pass # Indica que demomento no se procesa mas

print(type(Personas))

# Agregar caracteristicas a una clase

class Persona:
    def __init__(self):# Es el iniciador de un objeto
        # Atributos de instancia
        self.nombre = 'Juan'
        self.apellido = 'Perez'
        self.edad = 28

# Crear un objeto de una clase ya creada:

persona1 = Persona()
# Acceder a un atributo
print(persona1.nombre)