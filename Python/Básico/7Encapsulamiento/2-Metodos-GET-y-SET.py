# get = obtener/recuperar
# set = colocar/modificar


class Persona:
    # Para pasar como argumentos una tupla: *args | Para un diccionario: **kwargs | Tambien podemos cambiar el nombre a nuestro gusto
    def __init__(self, nombre, apellido, edad):
        self._nombre = nombre
        self.apellido = apellido
        self.edad = edad

    # Definimos metodo get
    @property# "Decorador" Modifica el comportamiento de nuestro metodo. De esta forma al colocarlo en el metodo "Nombre" indicamos que va
    # recuperar el atributo _nombre y de esta forma solo podremos haccederlo a través del método.
    def nombre(self):
        return self._nombre
    
    # Si queremos definir el método set para modificar el atributo de _nombre:

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre
    def mostrar_detalle(self):  # Se agrega siempre el metodo de instancia "self"
        print(f'Persona: {self.nombre} {self.apellido} {self.edad} {self.valores} {self.terminos}')




persona1 = Persona('Ruben', 'Pedroche', 34)
# Acceder al atributo nombre
print(persona1.nombre)
# De esta forma ya no estamos estamos accediendo directamente al atributo de nombre y tampoco hace falta "con @property" colocar ().
