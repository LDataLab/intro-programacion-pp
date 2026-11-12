from pathlib import Path

import duckdb
import pandas as pd

DB_PATH = Path(__file__).resolve().parents[3] / "data/db/ecobici.duckdb"


def myquery(sql: str) -> pd.DataFrame:
    """Ejecuta una consulta SQL y devuelve un DataFrame."""
    with duckdb.connect(str(DB_PATH), read_only=True) as con:
        return con.execute(sql).df()