# Empezamos a crear algunos objetos de la clase empleado y gerente
# Primero definiremos un método que hará mandar a imprimir el detalle de los objetos empleado o gerente.
# Así que, independientemente del tipo de dato empleado o gerente que reciba, vamos a poder ejecutar el método STR
# de cualquiera de los dos objetos.

# Asi que precisamente aqui es donde se va a aplicar el concepto de polimorfismo, ya que en tiempos de ejecución se 
# puede ejecutar cualquiera de los dos métodos, ya sea el método STR de la clse empleado o de la clase gerente. En primer 
# lugar definiremos un método.

from Parte1 import Empleado
from Gerente import Gerente

def imprimir_detalles(objeto):
    print(objeto)
    # Recordemos que esto de manera indirecta va a mandar a llamar el método STR, ya sea de la clase empleado o gerente. 
    # Aqui es donde se aplica el concepto de polimorfismo.
    print(type(objeto))
    # Para ver que tipo de objeto es al cual estamos apuntando.


# Empezamos a utilizar los objetos:

empleado = Empleado('Juan', 5000)
imprimir_detalles(empleado)

# Creamos una variable que apunte a la clase hija

gerente = Gerente('karla', 6000, 'Sistemas')
imprimir_detalles(gerente)