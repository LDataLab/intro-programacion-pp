"""API REST de ejemplo sobre la base de EcoBici (m13).

Variables de entorno (ver m11):
- API_TOKEN: token que deben enviar los clientes en el encabezado Authorization.

La base DuckDB se consulta con `myquery` (src/progra/tools/mydb.py).
"""

import os
from typing import Annotated

from fastapi import FastAPI, Header, HTTPException, Query

from progra.tools.mydb import DB_PATH, myquery

API_TOKEN = os.environ.get("API_TOKEN")

# Sin token la API no debe arrancar: es mejor fallar al inicio que aceptar peticiones sin protección.
if not API_TOKEN:
    raise RuntimeError("Define API_TOKEN en .envrc o .env antes de iniciar la API.")

app = FastAPI(title="API EcoBici", version="0.1.0")


def verificar_token(authorization: Annotated[str | None, Header()] = None) -> None:
    """Rechaza la petición si el encabezado Authorization no trae el token correcto."""
    if authorization != f"Bearer {API_TOKEN}":
        raise HTTPException(status_code=401, detail="Token inválido o ausente")


def consultar(sql: str, parametros: list | None = None) -> list[dict]:
    """Ejecuta SQL con myquery y devuelve filas como diccionarios."""
    if not DB_PATH.exists():
        raise HTTPException(status_code=500, detail=f"No existe la base: {DB_PATH}")
    return myquery(sql, parametros).to_dict(orient="records")


@app.get("/health")
def health() -> dict:
    """Verifica que la API está viva. No requiere token."""
    return {"estado": "ok"}


@app.get("/resumen")
def resumen(authorization: Annotated[str | None, Header()] = None) -> dict:
    verificar_token(authorization)
    filas = consultar(
        """
        SELECT
            COUNT(*) AS viajes,
            MIN(fecha_retiro) AS desde,
            MAX(fecha_retiro) AS hasta,
            ROUND(AVG(edad), 1) AS edad_promedio
        FROM clean.ecobici
        """
    )
    return filas[0]


@app.get("/viajes/por-genero")
def viajes_por_genero(authorization: Annotated[str | None, Header()] = None) -> list[dict]:
    verificar_token(authorization)
    return consultar(
        """
        SELECT genero, COUNT(*) AS viajes
        FROM clean.ecobici
        GROUP BY genero
        ORDER BY viajes DESC
        """
    )


@app.get("/estaciones/{estacion_id}/retiros")
def retiros_de_estacion(
    estacion_id: int,
    limite: Annotated[int, Query(ge=1, le=100)] = 10,
    authorization: Annotated[str | None, Header()] = None,
) -> list[dict]:
    verificar_token(authorization)
    filas = consultar(
        """
        SELECT fecha_retiro, bici, estacion_arribo
        FROM clean.ecobici
        WHERE estacion_retiro = ?
        ORDER BY fecha_retiro DESC
        LIMIT ?
        """,
        [estacion_id, limite],
    )
    if not filas:
        raise HTTPException(status_code=404, detail=f"La estación {estacion_id} no tiene retiros")
    return filas
