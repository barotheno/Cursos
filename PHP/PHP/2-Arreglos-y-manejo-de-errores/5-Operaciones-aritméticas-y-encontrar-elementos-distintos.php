<?php

    # Sumar valores del arreglo
    $numeros = [1, 20, 30, 15, 5, 10];
    $suma = array_sum($numeros);
    echo "Mi suma es ".$suma;

    # Encontrar diferencias entre arreglos
    $salonA = ['a1' => 'Juan', 'a2' => 'Susana'];
    $salonB = ['a1' => 'Juanito', 'a2' => 'Susana'];
    $diferencia = array_diff($salonA, $salonB);
    var_dump($diferencia);

?>