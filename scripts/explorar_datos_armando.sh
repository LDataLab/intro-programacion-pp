#!/usr/bin/env bash

echo "Explorando datos"

date

echo "Directorio:"
pwd

echo "Archivos:"
ls -lh

echo "Número de líneas:"
wc -l datos_agua.csv

echo "Primeras cinco filas:"
head -n 5 datos_agua.csv
