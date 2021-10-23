from Persona import Persona

print('Creación de objetos'.center(50,'-'))
persona1 = Persona('Karla', 'Gomez', 30)
persona1.mostrar_detalle()

print('Eliminacion de objetos'.center(50,'-'))
del persona1
# A través de una función en este caso en la clase Persona, ver la funcion en archivo Persona.py