from Dominio.pelicula import Pelicula
from servicio.catalogo_peliculas import CatalogoPeliculas as cp
opcion = None

while opcion != 4:
    try:
        print('Opciones: ')
        print('1. Agregar peliculas')
        print('2. Listar Películas')
        print('3. Eliminar catálogo peliculas')
        print('4. Salir')
        opcion = int(input('Escribe tu opcion entre 1 y 4: '))

        if opcion == 1:
            nombre_pelicula = input('Introduce el nombre de la pelicula: ')
            pelicula = Pelicula(nombre_pelicula)
            cp.agregar_pelicula(pelicula)
        elif opcion ==2:
            cp.listar_peliculas()
        elif opcion ==3:
            cp.eliminar_peliculas()
    except Exception as e:
        print(f'Ocurrió un error {e}')
        opcion = None
else:
    print('Un placer viejo amigo')