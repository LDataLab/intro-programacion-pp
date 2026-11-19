from fastapi import FastAPI
from pydantic import BaseModel
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier

# Crear la aplicación
app = FastAPI(title="Clasificador de flores Iris")

# Cargar los datos
iris = load_iris()

# Entrenar un modelo de clasificación
modelo = DecisionTreeClassifier(random_state=42)
modelo.fit(iris.data, iris.target)


# Variables que recibe nuestra API
class Flor(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float


# Ruta principal
@app.get("/")
def inicio():
    return {"mensaje": "Bienvenido al clasificador Iris"}


# Ruta de predicción
@app.post("/predict")
def predecir(flor: Flor):
    datos = [[
        flor.sepal_length,
        flor.sepal_width,
        flor.petal_length,
        flor.petal_width,
    ]]

    prediccion = modelo.predict(datos)[0]
    especie = iris.target_names[prediccion]

    return {"especie": especie}

