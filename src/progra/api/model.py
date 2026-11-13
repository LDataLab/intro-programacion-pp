import datetime
from pathlib import Path

import joblib

BASE_DIR = Path(__file__).resolve(strict=True).parent
TODAY = datetime.date.today()

def clima_del_dia(mes, nublado, turno):
    # Modelo de predicción
    if nublado and (mes in ["junio", "julio", "agosto"]):
        posibilidad = "Alta"
    elif nublado and turno.lower() == "tarde":
        posibilidad = "Moderada"
    elif mes in ["noviembre", "diciembre", "enero"] and not nublado:
        posibilidad = "Baja"
    else:
        posibilidad = "Baja"

    return {"Posibilidad": posibilidad}



def pack(input_data):
    output = {}

    mes = input_data["mes"]
    nublado = input_data["nublado"] 
    turno = input_data["turno"] 

    date = TODAY.strftime("%d/%m/%Y")
    
    posibilidad = clima_del_dia(mes, nublado, turno)
    output = {
                "date": date,
                "¿Qué tan posible es que llueva hoy": posibilidad,
                }

    return output
