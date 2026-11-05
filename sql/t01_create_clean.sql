CREATE SCHEMA IF NOT EXISTS clean;

CREATE SCHEMA IF NOT EXISTS clean;

CREATE OR REPLACE TABLE clean.ecobici AS
SELECT
    Genero_Usuario::VARCHAR AS genero,
    Edad_Usuario::SMALLINT AS edad,
    Bici::INTEGER AS bici,
    Ciclo_Estacion_Retiro::SMALLINT AS estacion_retiro,
    (Fecha_Retiro::DATE + Hora_Retiro::TIME) AS fecha_retiro,
    Ciclo_Estacion_Arribo::SMALLINT AS estacion_arribo,
    (Fecha_Arribo::DATE + Hora_Arribo::TIME) AS fecha_arribo
FROM read_csv('data/raw/ecobici-2014-*.csv');

