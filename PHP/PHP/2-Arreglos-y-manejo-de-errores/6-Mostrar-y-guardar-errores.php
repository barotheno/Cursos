<?php 

    # Desactivar toda notificacion de error
    error_reporting(0);
    $nombre = 'Hola';
    echo $nombre;
    echo $nombres;

    # Guardar error en un log
    ini_set("log_errors", 1);
    ini_set("error_log", "php-error.log");
    error_log("Hay un error");



?>