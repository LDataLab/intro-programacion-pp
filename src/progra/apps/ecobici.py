"""Ejemplo docente para m11: reporte parcial con Dash y DuckDB.

No es una solución de la Tarea 4. Contiene dos visualizaciones de ejemplo:
una estática y una interactiva, para discutir su implementación.

Requiere el paquete `progra` del repositorio de la clase y su función
`progra.tools.mydb.myquery`, además de `data/db/ecobici.duckdb`.

Desde la raíz del proyecto:
    uv run python src/progra/analysis/app_ecobici_guia.py
"""

import plotly.express as px
from dash import Dash, Input, Output, dcc, html

from progra.db.mydb import myquery


# ------------------------------------------------------------
# 1. Presentación: colores y estilos (solo apariencia visual)
# ------------------------------------------------------------
COLORS = {
    "background": "#f5f7fa",
    "paper": "#ffffff",
    "ink": "#17324d",
    "muted": "#52657a",
    "accent": "#167a76",
    "border": "#dce4eb",
}

PAGE_STYLE = {
    "maxWidth": "960px",
    "margin": "40px auto",
    "padding": "0 20px 40px",
    "fontFamily": "Arial, sans-serif",
    "color": COLORS["ink"],
}

CARD_STYLE = {
    "backgroundColor": COLORS["paper"],
    "border": f"1px solid {COLORS['border']}",
    "borderRadius": "12px",
    "padding": "22px",
    "marginTop": "18px",
}


# ------------------------------------------------------------
# 2. Consultas: DuckDB agrupa, Python recibe resultados pequeños
# ------------------------------------------------------------
# Primera pregunta: ¿cómo varía el número de retiros por hora?
# Un renglón del resultado = una hora del día, NO un viaje.
retiros_hora = myquery(
    """
    SELECT
        EXTRACT(hour FROM fecha_retiro) AS hora,
        COUNT(*) AS total_retiros
    FROM clean.ecobici
    WHERE fecha_retiro IS NOT NULL
    GROUP BY 1
    ORDER BY 1;
    """
)

# Segunda pregunta: ¿cómo cambia el patrón por género registrado?
# Se agregan los datos EN SQL, no se copian las primeras 10,000 filas.
retiros_hora_genero = myquery(
    """
    SELECT
        EXTRACT(hour FROM fecha_retiro) AS hora,
        COALESCE(genero, 'Sin dato') AS genero,
        COUNT(*) AS total_retiros
    FROM clean.ecobici
    WHERE fecha_retiro IS NOT NULL
    GROUP BY 1, 2
    ORDER BY 1, 2;
    """
)

# Los valores exactos proceden de la base del curso; no se inventan cifras.
total_viajes = int(retiros_hora["total_retiros"].sum())
generos = sorted(retiros_hora_genero["genero"].astype(str).unique())


# ------------------------------------------------------------
# 3. Figura estática: no necesita callback
# ------------------------------------------------------------
fig_horas = px.bar(
    retiros_hora,
    x="hora",
    y="total_retiros",
    title="Retiros registrados por hora del día",
    labels={"hora": "Hora del retiro", "total_retiros": "Número de retiros"},
)
fig_horas.update_traces(marker_color=COLORS["accent"])
fig_horas.update_layout(
    template="plotly_white",
    paper_bgcolor=COLORS["paper"],
    plot_bgcolor=COLORS["paper"],
    margin={"l": 32, "r": 20, "t": 65, "b": 35},
    xaxis={"dtick": 2},
)


# ------------------------------------------------------------
# 4. Layout: un reporte debe tener argumento, contexto y límites
# ------------------------------------------------------------
app = Dash(__name__, title="Ecobici | Reporte de ejemplo")

app.layout = html.Div(
    style={"backgroundColor": COLORS["background"], "minHeight": "100vh"},
    children=[
        html.Main(
            style=PAGE_STYLE,
            children=[
                html.P("EJEMPLO DOCENTE · M11", style={"color": COLORS["accent"], "fontWeight": "bold"}),
                html.H1("¿Cuándo se registran los retiros de Ecobici?"),
                html.P(
                    "Un reporte parcial para aprender a combinar consultas SQL, "
                    "interpretaciones y controles en Dash.",
                    style={"color": COLORS["muted"], "fontSize": "17px"},
                ),
                html.Section(
                    style=CARD_STYLE,
                    children=[
                        html.H2("Contexto y pregunta"),
                        html.P(
                            "Partimos de viajes registrados en la base de Ecobici. "
                            "Nos preguntamos cómo cambia la cantidad de retiros según "
                            "la hora del día. El conteo de retiros no mide disponibilidad "
                            "de bicicletas en una estación."
                        ),
                        html.P(
                            f"Registros con hora de retiro válida: {total_viajes:,}.",
                            style={"fontWeight": "bold", "color": COLORS["accent"]},
                        ),
                    ],
                ),
                html.Section(
                    style=CARD_STYLE,
                    children=[
                        html.H2("1. Patrones por hora"),
                        html.P("¿Cómo se distribuyen los retiros registrados a lo largo del día?"),
                        dcc.Graph(id="grafico-estatico", figure=fig_horas),
                        html.P(
                            "Para interpretar la gráfica, identifica las horas de mayor y "
                            "menor frecuencia. Recuerda que aquí se acumulan retiros "
                            "de todos los días incluidos en la base.",
                            style={"color": COLORS["muted"]},
                        ),
                    ],
                ),
                html.Section(
                    style=CARD_STYLE,
                    children=[
                        html.H2("2. Explorar por género registrado"),
                        html.P(
                            "Selecciona una categoría para observar el patrón horario "
                            "de sus viajes registrados."
                        ),
                        dcc.Dropdown(
                            id="filtro-genero",
                            options=[{"label": "Todas las categorías", "value": "__todos__"}]
                            + [{"label": valor, "value": valor} for valor in generos],
                            value="__todos__",
                            clearable=False,
                        ),
                        dcc.Graph(id="grafico-interactivo"),
                        html.P(id="texto-interactivo", style={"color": COLORS["muted"]}),
                    ],
                ),
                html.Section(
                    style=CARD_STYLE,
                    children=[
                        html.H2("3. Fuente y limitaciones"),
                        html.P(
                            "Fuente: tabla clean.ecobici del proyecto de clase. "
                            "La cobertura temporal y el origen exacto deben verificarse "
                            "con los metadatos del dataset antes de publicar un reporte."
                        ),
                        html.P(
                            "Los datos describen viajes registrados, no el inventario "
                            "de bicicletas. Las diferencias por género no deben "
                            "interpretarse automáticamente como diferencias de uso "
                            "de toda la población de la ciudad."
                        ),
                    ],
                ),
                html.P(
                    "Actividad: ¿qué otra pregunta relevante añadirías y qué tabla "
                    "de la capa model construirías para responderla?",
                    style={"marginTop": "24px", "fontWeight": "bold"},
                ),
            ],
        )
    ],
)


# ------------------------------------------------------------
# 5. Callback: control -> filtro -> figura y texto
# ------------------------------------------------------------
@app.callback(
    Output("grafico-interactivo", "figure"),
    Output("texto-interactivo", "children"),
    Input("filtro-genero", "value"),
)
def actualizar_comparacion(genero_seleccionado):
    """Ejemplo de una función que devuelve DOS outputs en orden."""
    if genero_seleccionado == "__todos__":
        # Evita doble agregación de categorías al agrupar por hora.
        datos = retiros_hora.copy()
        etiqueta = "todas las categorías"
    else:
        datos = retiros_hora_genero.loc[
            retiros_hora_genero["genero"] == genero_seleccionado,
            ["hora", "total_retiros"],
        ].copy()
        etiqueta = genero_seleccionado

    figura = px.line(
        datos,
        x="hora",
        y="total_retiros",
        markers=True,
        labels={"hora": "Hora del retiro", "total_retiros": "Número de retiros"},
        title=f"Retiros por hora: {etiqueta}",
    )
    figura.update_traces(line_color=COLORS["accent"])
    figura.update_layout(
        template="plotly_white", paper_bgcolor=COLORS["paper"],
        plot_bgcolor=COLORS["paper"], xaxis={"dtick": 2},
        margin={"l": 32, "r": 20, "t": 65, "b": 35},
    )

    lectura = (
        f"Se muestran retiros de {etiqueta}. "
        "Para comparar grupos de distinto tamaño, podríamos usar "
        "proporciones por hora en vez de conteos absolutos."
    )
    return figura, lectura


# ------------------------------------------------------------
# 6. Ejecución: local (no publicación en Internet)
# ------------------------------------------------------------
if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=8050)
