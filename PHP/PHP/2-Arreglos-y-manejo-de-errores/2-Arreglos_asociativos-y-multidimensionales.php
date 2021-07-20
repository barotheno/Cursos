<?php
    /**
     * QUE ES UN ARREGLO??
     * 
     *      @ Es una colección de datos multiples ordenados en filas (unidimensionales) o en columnas y filas (multidimensionales)
     *      @ Pueden ser indexados y asociativos
     * 
     *      ## ARREGLOS INDEXADOS
     * 
     *      Utilizan índices [0, 1 .. n]
     *      Empezamos siempre en el índice 0 y su total empieza siempre en 1
     * 
     *          $numeros = [];  $numeros = array();
     * 
     *      Para seleccionar un valor del arreglo lo hacemos asi:
     * 
     *          $numero[0]
     */

    $lenguajes = ["PHP", "Python", "C++", "Java"];
    echo $lenguajes[1];
    /**
     * ARREGLOS ASOCIATIVOS
     * 
     * ## Serie de espacios que almacenan datos
     * ## Nosotros indicamos la relación con una llave, clave o nombre
     * 
     */

    $lenguajes1 = ["lenguaje1" => 'PHP', "lenguaje2" => 'Java'];
    echo $lenguajes1["lenguaje2"];

    /**
     * ARREGLOS MULTIDIMENSIONALES
     * 
     * Primero se indica la fila y después la columna
     */

    /** CREACION DE ARREGLOS
     * 
     *  Al crear arreglos es posible ver la estructura del arreglo con las 2 siguientes funciones:
     * 
     *      @ var_dump($arreglo) o print_r($arreglo)
     */

    var_dump($lenguajes);
    print_r($lenguajes);

    
?>