#!/usr/bin/env bash

echo "Explorando datos"
<<<<<<< HEAD

=======
echo "hola"
>>>>>>> 2b94b50c673bc8efe6dd2e805a445730bc298099
date

echo "Directorio:"
pwd

echo "Archivos:"
ls -lh

<<<<<<< HEAD
echo "Número de líneas:"
wc -l ../data/datos_agua.csv

echo "Primeras cinco filas:"
head -n 5 ../data/datos_agua.csv
=======

base="data/datos_agua.csv"

echo "$base"

echo "Número de líneas:"
wc -l "$base"

echo "Primeras cinco filas:"
head -n 5 "$base"
>>>>>>> 2b94b50c673bc8efe6dd2e805a445730bc298099
