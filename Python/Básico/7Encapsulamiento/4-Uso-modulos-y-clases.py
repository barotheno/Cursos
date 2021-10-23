# Para poder utilizar modulos, es decir clases desde otros archivos hacemos lo siguiente:

# 1) Indicamos de que modulo "Archivo" queremos importar la clase, para eso usamos from:
from Persona import Persona

persona1 = Persona('Karla', 'Gomez', 30)
persona1.mostrar_detalle()