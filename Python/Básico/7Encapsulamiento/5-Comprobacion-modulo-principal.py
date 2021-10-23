

# Cuando importamos un modulo, encontramos que también se ejecuta el codigo del módulo en nuestro archivo actual

from Persona import Persona

persona1 = Persona('Karla', 'Gomez', 30)
persona1.mostrar_detalle()
