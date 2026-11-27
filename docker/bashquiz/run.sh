#!/bin/bash

echo "Mini quiz de bash"
echo

read -p "1) ¿Qué comando sirve para listar archivos? " r1
if [[ "$r1" == "ls" ]]; then
    echo "Correcto"
else
    echo "Incorrecto"
fi

read -p "2) ¿Cómo regresas a la raíz de tu usuario? " r2
if [[ "$r2" == "cd" ]]; then
    echo "Correcto"
else
    echo "Incorrecto"
fi

read -p "3) ¿Con qué comando copias archivos? " r3
if [[ "$r3" == "cp" ]]; then
    echo "Correcto"
else
    echo "Incorrecto"
fi

echo "Fin del quiz"
