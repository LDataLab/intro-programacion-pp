"""Métricas simples para las prácticas de Python."""


def promedio(valores):
    """Calcula el promedio de una secuencia no vacía."""
    if not valores:
        raise ValueError("La secuencia no puede estar vacía")
    return sum(valores) / len(valores)


def calcular_area(largo, ancho):
    """Calcula el área de un rectángulo."""
    return largo * ancho


def calcular_perimetro(largo, ancho):
    """Calcula el perímetro de un rectángulo."""
    return 2 * (largo + ancho)
