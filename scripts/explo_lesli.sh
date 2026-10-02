#!/usr/bin/env bash

echo "Explorando datos"

date

echo "Directorio:"
pwd

echo "Archivos:"
ls -lh

echo "Número de líneas:"
wc -l ../data/datos_agua.csv

echo "Primeras cinco filas:"
head -n 5 ../data/datos_agua.csv
