<?php

    # Arreglos y sus funciones nativas:
    $cadena = '';
    $arreglo = [];
    $videojuegos = [
        'FIFA', 'Fortnite', 'Red Dead',
        'Call of Dutty', 'Battlefield',
        'Pokémon', 'GTA', 'The Sims'
    ];

    # Como saber si un arreglo esta Vacio:
    var_dump(empty($arreglo));
    var_dump(empty($videojuegos));

    # Como saver si existe un elemento:
    var_dump(isset($videojuegos[2]));

    # Contar los elementos de un arreglo:
    echo count($videojuegos);

    # Traer antepenultimo elemento:

    $posicion = count($videojuegos) - 2;
    echo $videojuegos[$posicion];

    # Ordenar el arreglo de manera alfabética:
    sort($videojuegos);
    var_dump($videojuegos);

    # Ordenar alfabeticamente sin perder su indice:
    asort($videojuegos);
    var_dump($videojuegos);

    # Ordenar de manera inversa:

    rsort($videojuegos);
    var_dump($videojuegos);

    # Dividir un arreglo
    $dividir = array_chunk($videojuegos, 2);
    var_dump($dividir);

    # Dividir el arreglo y eliminar lo anterior

    var_dump( array_slice($videojuegos, 3));

    # Unir arreglos

    $frutas = ['platano', 'uva', 'manzana'];
    $verduras = ['chile', 'tomate'];
    $unir = array_merge($frutas, $verduras);
    var_dump($unir);

    # Agregar uno o más elementos al final del arreglo
    array_push($videojuegos, 'Smash Bros');
    var_dump(($videojuegos));

    # Buscar un elemento en el arreglo
    $calAlumnos = [10, 2, 4, 7, 100, 8,6];
    $buscar = array_search(10, $calAlumnos);



?>