# app_ecobici_simple.py
import pandas as pd
import plotly.express as px
from dash import Dash, dcc, html, Input, Output

from progra.tools.mydb import myquery


# -------------------------------------------------------
# Carga de datos desde DuckDB (con myquery)
# -------------------------------------------------------
query = """
select
    genero,
    edad,
    estacion_retiro,
    estacion_arribo
from clean.ecobici
limit 10000;
"""

df = myquery(query)


# -------------------------------------------------------
# Inicialización de la app Dash
# -------------------------------------------------------
app = Dash(__name__) # Observa
# __name__ hace referencia al nombre del archivo actual 


# -------------------------------------------------------
# Definición del layout (estructura visual)
# -------------------------------------------------------
app.layout = html.Div([
    html.H1("Mi primera app"),
    html.H2("Dashboard Ecobici CDMX"),
    dcc.Dropdown(
        id='variable',
        options=[
            {'label': 'Género', 'value': 'genero'},
            {'label': 'Edad', 'value': 'edad'}
        ],
        value=None,
		placeholder="Selecciona una variable",
        clearable=True
    ),
    dcc.Graph(id='grafico', figure={}), # Gráfico vacío al inicio
    html.Hr(),  # línea divisoria
    html.H3("Edad promedio por género"),
    dcc.Graph(id='grafico_promedios')  # segundo gráfico

])


# -------------------------------------------------------
# Definición de los callbacks (interactividad)
# -------------------------------------------------------
@app.callback( # Decorador envuelve la función con otra función
    [Output('grafico', 'figure'),
    Output('grafico_promedios', 'figure')],
    Input('variable', 'value')
)
def actualizar_grafico(variable):
    """Actualiza el gráfico cuando cambia la variable del Dropdown"""
    if not variable:
        return {},{}
    fig1 = px.histogram(
        df,
        x=variable,
        color='genero',
        title=f"Distribución de {variable}",
        barmode='group'
    )
    # Segundo gráfico: edad promedio por género
    promedio = df.groupby('genero')['edad'].mean().reset_index()
    fig2 = px.bar(
        promedio,
        x='genero',
        y='edad',
        title="Edad promedio por género",
        text_auto=".2f"
    )
    fig1.update_layout(template='plotly_white')
    fig2.update_layout(template='plotly_white')
    return fig1, fig2

# En este caso, el decorador app.callback registra actualizar_grafico 
# como una función que se ejecutará automáticamente 
# cuando cambie el valor de entrada (Input('variable', 'value')).

# -------------------------------------------------------
# Ejecución de la app
# -------------------------------------------------------
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8050)

