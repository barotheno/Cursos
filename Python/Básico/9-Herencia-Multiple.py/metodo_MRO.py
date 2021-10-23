# uando estamos trabajando con herencia múltiple, es importante, es importante saver el orden en el que se mandan a llamar las clases padre.
# Para ello tenemos el método:
#   MRO - Method Resolution Order

# Nos permite conocer la gerarquía de clases de en clase que mandamos llamar este metodo.

from cuadrado import Cuadrado

print(Cuadrado.mro())