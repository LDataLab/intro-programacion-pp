import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

class AnalisisBiciCDMX:
    """Clase para análisis exploratorio y visual de viajes Ecobici (CDMX)"""

    def __init__(self, df):
        """
        Inicializa el análisis con un DataFrame ya cargado.
        Parámetros:
            df (pd.DataFrame): Datos de viajes Ecobici con columnas:
                ['genero', 'edad', 'bici', 'estacion_retiro',
                 'fecha_retiro', 'estacion_arribo', 'fecha_arribo']
        """
        self.df = df.copy()

    # ---------------------------
    # 1. Preparar datos
    # ---------------------------
    def preparar_datos(self):
        """Limpia y genera columnas derivadas a partir de los timestamps."""
        if self.df is None or self.df.empty:
            raise ValueError("No hay datos cargados o el DataFrame está vacío.")

        # Calcular duración en minutos
        self.df['duracion_min'] = (
            self.df['fecha_arribo'] - self.df['fecha_retiro']
        ).dt.total_seconds() / 60

        # Crear columnas auxiliares para análisis temporal
        self.df['hora'] = self.df['fecha_retiro'].dt.hour
        self.df['dia_semana'] = self.df['fecha_retiro'].dt.day_name()

        # Limpiar nulos y viajes con duración negativa
        self.df = self.df.dropna(subset=['duracion_min'])
        self.df = self.df[self.df['duracion_min'] > 0]

        print("Datos preparados correctamente.")
        return self.df

    # ---------------------------
    # 2. Resumen descriptivo
    # ---------------------------
    def resumen(self):
        """Imprime un resumen general de los datos."""
        print("Total de viajes:", len(self.df))
        print("Bicicletas únicas:", self.df['bici'].nunique())
        print("Estaciones de retiro:", self.df['estacion_retiro'].nunique())
        print("Estaciones de arribo:", self.df['estacion_arribo'].nunique())
        print("Usuarios con edad registrada:", self.df['edad'].notna().sum())
        print("Duración promedio (min):", round(self.df['duracion_min'].mean(), 2))

    # ---------------------------
    # 3. Visualizaciones
    # ---------------------------
    def viajes_por_hora(self):
        """Número de viajes por hora del día."""
        plt.figure(figsize=(8,4))
        sns.countplot(x='hora', data=self.df, color='steelblue')
        plt.title("Viajes por hora del día")
        plt.xlabel("Hora del día")
        plt.ylabel("Número de viajes")
        plt.show()

    def estaciones_populares(self, top=10):
        """Top estaciones más utilizadas para retiro."""
        top_est = self.df['estacion_retiro'].value_counts().head(top)
        plt.figure(figsize=(8,4))
        sns.barplot(x=top_est.index, y=top_est.values, color='salmon')
        plt.title(f"Top {top} estaciones más usadas (retiro)")
        plt.xlabel("Número de viajes")
        plt.ylabel("Estación")
        plt.show()

    def duracion_por_dia_semana(self):
        """Duración promedio por día de la semana."""
        orden_dias = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
        promedio = self.df.groupby('dia_semana')['duracion_min'].mean().reindex(orden_dias)
        plt.figure(figsize=(8,4))
        sns.barplot(x=promedio.index, y=promedio.values, color='mediumseagreen')
        plt.title("Duración promedio por día de la semana")
        plt.xlabel("Día de la semana")
        plt.ylabel("Duración (min)")
        plt.xticks(rotation=45)
        plt.show()
