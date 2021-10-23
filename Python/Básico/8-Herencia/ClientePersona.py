from IntroHerencia import * #Con * importamos todas las clases y funciones


# Creamos un objeto
persona1 = Persona('Juan', 28)
print(persona1)
# Si corremos el codigo nos lanzará lo siguiente
# <IntroHerencia.Persona object at 0x7febc79ffbb0> "La referencia en memoria donde se hubica el objeto"
# Para solucionar esto, podemos agregar un método a la clase llamado str.

# Si creamos un objeto de empleado podremos ver que al ser hijo de Persona, toma ya como referencia el método str:

empleado1 = Empleados('Ruben', 30, 5000)
print(empleado1)

# Si nos fimaos, no sale el sueldo cuando se corre el codigo, para ellos sobrescribimos el método str en la clase hija, pero esta ved
# solo necesitamos añadir {self.sueldo}