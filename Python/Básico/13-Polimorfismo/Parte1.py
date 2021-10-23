# Polimorfismo significa múltiples formas en tiempo de ejecución
# Por ejemplo si creamos un objeto de la clase empleado, podemos crear una variable que apunte a este objeto y entonces,
# si esta variable está apuntando a un objeto de la clase empleado que contiene ciertos atributos y también ciertos
# métodos como el método STR para mandar imprimir el detalle de este objeto, entonces esta variable va a mandar a imprimir
# el método STR con el detalle de cada uno de nuestros atributos.

class Empleado:
    def __init__(self,nombre, sueldo):
        self.nombre = nombre 
        self.sueldo = sueldo

    def __str__(self):
        return f'Empleado: [Nombre: {self.nombre}, Sueldo: {self.sueldo}]'

#Creando otra clase hija de Empleado sobrescribiremos el metodo str