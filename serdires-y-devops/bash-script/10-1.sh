#!/usr/bin/env bash


echo "Selecciones su lenguaje de programación favorito: "
PS3="
8===D "
select lenguaje in Bash Java C++ PHP
do
    echo "buena elección"
done