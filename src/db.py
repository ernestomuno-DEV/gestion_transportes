from supabase import create_client, Client
import streamlit as st
from .utils.limpieza import taller_limpieza



@st.cache_resource
def conexion() -> Client:
    url = st.secrets["supabase"]['url']
    key = st.secrets["supabase"]['key']
    return create_client(url, key)


@st.cache_data(ttl=60)
def obtener_datos(tabla: str, taller: str):
    supabase = conexion()
    try:
        response = supabase.table(tabla).select("*").eq("taller", taller).execute()
        print('todo ok')
        return response.data
    except Exception as e:
        st.error(f"Error al obtener datos de la tabla {tabla}: {e}")
        print(f"Error al obtener datos de la tabla {tabla}: {e}")
        return []


def registrar_datos(data: dict):
    data_lista = taller_limpieza(data)
    supabase = conexion()
    try:
        payload = {
            "taller" : data_lista.get("taller"),
            "fecha": data_lista.get("fecha"),
            "hora_entrada": data_lista.get("hora_entrada"),
            "economico": data_lista.get("economico"),
            "hora_salida": data_lista.get("hora_salida"),
            "conductor": data_lista.get("conductor"),
            "falla_reportada": data_lista.get("falla_reportada"),
            "mecanico": data_lista.get("mecanico"),
            "nota": data_lista.get("nota")
        }
        response = supabase.table(data_lista.get("tabla")).insert(payload).execute()
        return response.data
    except Exception as e:
        st.error(f"Error al registrar datos en la tabla")
        return None