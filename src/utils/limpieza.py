import pandas as pd
from datetime import time


def taller_limpieza(data: dict) -> dict:
    return {
        "tabla": data.get("tabla"),
        "taller": data.get("taller"),
        "fecha": pd.to_datetime(data.get("fecha")).strftime("%Y-%m-%d") if data.get("fecha") else None,
        "hora_entrada": limpiar_hora(data.get("hora_entrada")),
        "economico": data["economico"].strip().upper(),
        "hora_salida": limpiar_hora(data.get("hora_salida")),
        "conductor": data.get("conductor"),
        "falla_reportada": data.get("falla_reportada"),
        "mecanico": data.get("mecanico"),
        "nota": data.get("nota")
    }

def limpiar_hora(dato):

    if not dato:
        return None

    if isinstance(dato, time):
        return dato.strftime("%H:%M") 