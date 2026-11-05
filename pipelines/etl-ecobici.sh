#!/bin/bash

# Pipeline de descarga de datos para ecobici

# 1. Primero descargamos los datos
curl https://ecobici.cdmx.gob.mx/wp-content/uploads/2022/08/2014-01.csv > data/raw/ecobici-2014-01.csv

curl https://ecobici.cdmx.gob.mx/wp-content/uploads/2022/08/2014-02.csv > data/raw/ecobici-2014-02.csv

# Carga de esquema clean dentro de duckdb

duckdb data/db/ecobici.duckdb -f sql/t01_create_clean.sql
