import streamlit as st

#Enrutamiento de paginas
gestion  = st.Page("pages/gestion.py", title= 'Gestion', default=True)
registro = st.Page("pages/registro.py", title= 'Registro')

navegacion = st.navigation(
    [gestion, registro]
)

navegacion.run()