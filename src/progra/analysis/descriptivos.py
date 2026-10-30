import numpy as np


def resumen(valores):
    percentiles = [10, 30, 50, 70, 80, 90, 95, 99]
    resultado = {}

    for p in percentiles:
        resultado[f"percentil {p}"] = float(np.percentile(valores, p))

    resultado["media"] = float(valores.mean())
    resultado["max"] = float(valores.max())
    resultado["min"] = float(valores.min())

    return resultado