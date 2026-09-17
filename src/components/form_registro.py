import streamlit as st
from ..db import registrar_datos
import pandas as pd

"""
def render_form_registro(servicio: str, tabla:str):
   with st.form(f'Registro de datos {servicio}', clear_on_submit=True):
      fecha = st.date_input(f'Fecha {servicio}')
      hora_entrada = st.time_input(f'Hora de entrada {servicio}', value=None)
      economico = st.text_input(f'economico {servicio}')
      hora_salida = st.time_input(f'Hora de salida {servicio}', value=None)
      conductor = st.text_input(f'Conductor {servicio}')
      falla_reportada = st.text_area(f'Falla reportada {servicio}')
      mecanico = st.text_input(f'Mecanico {servicio}')
      nota = st.text_area(f'Nota {servicio}')
      guardar = st.form_submit_button(f'Guardar datos {servicio}')

      if guardar and fecha and economico and falla_reportada:
         nuevo_registro = registrar_datos(dict(
            taller=servicio,
            tabla=tabla,
            fecha=str(fecha),
            hora_entrada=str(hora_entrada),
            economico=economico,
            hora_salida=str(hora_salida),
            conductor=conductor,
            falla_reportada=falla_reportada,
            mecanico=mecanico,
            nota=nota
            ))
         if nuevo_registro:
            st.success(f'Datos de {servicio} guardados correctamente.')
"""

def render_form_registro(servicio: str, tabla: str):
    with st.form(f'form_registro_{servicio}', clear_on_submit=True):
        col1, col2 = st.columns(2)
        with col1:
            fecha = st.date_input(f'Fecha')
            hora_entrada = st.time_input(f'Hora de entrada', value=None)
            economico = st.text_input(f'Número Económico')
            hora_salida = st.time_input(f'Hora de salida', value=None)
        with col2:
            conductor = st.text_input(f'Conductor')
            mecanico = st.text_input(f'Mecánico')
            falla_reportada = st.text_area(f'Falla reportada')
            nota = st.text_area(f'Notas')

        guardar = st.form_submit_button(f'Guardar datos {servicio}', use_container_width=True)

        if guardar:
            if not economico or not falla_reportada:
                st.warning("El número económico y la falla son obligatorios.")
                return

            nuevo_registro = registrar_datos({
                "taller": servicio,
                "tabla": tabla,
                "fecha": fecha,
                "hora_entrada": hora_entrada,   # Se envía el objeto time o None
                "economico": economico,
                "hora_salida": hora_salida,     # Se envía el objeto time o None
                "conductor": conductor,
                "falla_reportada": falla_reportada,
                "mecanico": mecanico,
                "nota": nota
            })
            if nuevo_registro:
                st.success(f'Unidad {economico.upper()} registrada en {servicio}.')

         
         

