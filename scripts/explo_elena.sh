#!/usr/bin/env bash

echo "Explorando datos"
echo "hola"
echo "adions"
date

echo "Directorio:"
pwd

echo "Archivos:"
ls -lh


base="data/datos_agua.csv"

echo "$base"

echo "Número de líneas:"
wc -l "$base"

echo "Primeras cinco filas:"
head -n 5 "$base"
