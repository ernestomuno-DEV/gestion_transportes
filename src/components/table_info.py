from ..db import obtener_datos
import streamlit as st
import pandas as pd

def render_table_info(servicio: str, tabla: str):
    df = pd.DataFrame(obtener_datos(tabla, servicio))
    df['fecha'] = pd.to_datetime(df['fecha'])

    st.subheader(f'servicio de {servicio}')
    col1, col2 = st.columns(2)

    

    with col1:
        min_date =  df['fecha'].min().date()
        max_date =  df['fecha'].max().date()
        rango=st.date_input(f'Selecciona una fecha para {servicio}',value=[min_date,max_date], min_value=min_date, max_value=max_date)

    with col2:
        camiones = df['economico'].unique()
        seleccionado = st.multiselect(f'Camiones {servicio}', options=camiones, default=camiones )


    if len(rango) == 2:
        inicio, fin = rango
        df_filtrado = df[
        (df['fecha'].dt.date >= inicio) &
        (df['fecha'].dt.date <= fin) &
        (df['economico'].isin(seleccionado))]

        st.dataframe(df_filtrado)

    else:
        df_filtrado = df[df['economico'].isin(seleccionado)]
        st.dataframe(df_filtrado)