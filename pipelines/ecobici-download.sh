#!/bin/bash

# Pipeline de descarga de datos para ecobici

# 1. Primero descargamos los datos
curl https://ecobici.cdmx.gob.mx/wp-content/uploads/2022/08/2014-01.csv > data/ecobici-2014-01.csv
curl https://ecobici.cdmx.gob.mx/wp-content/uploads/2022/08/2014-02.csv > data/ecobici-2014-02.csv

