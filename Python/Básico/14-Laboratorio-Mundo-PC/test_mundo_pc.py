from teclado import Teclado
from monitor import Monitor
from raton import Raton
from computadora import Computadora
from orden import Orden

teclado1 = Teclado('HP', 'USB')
monitor1 = Monitor('HP', 15)
raton1 = Raton('HP', 'USB')
computadora1 = Computadora('HP', monitor1, teclado1, raton1)

teclado2 = Teclado('HP', 'WIFI')
monitor2 = Monitor('Racer', 27)
raton2 = Raton('Racer', 'USB')
computadora2 = Computadora('MSI', monitor1, teclado1, raton1)

computadoras1 = [computadora1, computadora2]
orden1 = Orden(computadoras1)
print(orden1)
