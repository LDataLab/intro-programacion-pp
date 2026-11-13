"""API REST de ejemplo sobre la base de EcoBici (m11).

La base DuckDB se consulta con `myquery` (src/progra/tools/mydb.py).
"""

from typing import Annotated

from fastapi import FastAPI, HTTPException, Query

from progra.db.mydb import DB_PATH, myquery

app = FastAPI(title="API EcoBici", version="0.1.0")


def consultar(sql: str, parametros: list | None = None) -> list[dict]:
    """Ejecuta SQL con myquery y devuelve filas como diccionarios."""
    if not DB_PATH.exists():
        raise HTTPException(status_code=500, detail=f"No existe la base: {DB_PATH}")
    return myquery(sql).to_dict(orient="records")


@app.get("/health")
def health() -> dict:
    """Verifica que la API está viva."""
    return {"estado": "ok"}


@app.get("/resumen")
def resumen() -> dict:
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
def viajes_por_genero() -> list[dict]:
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
) -> list[dict]:
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
