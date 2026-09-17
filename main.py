import streamlit as st

st.set_page_config(page_title='Gestion Transportes',layout='wide' )
#Enrutamiento de paginas
gestion  = st.Page("pages/gestion.py", title= 'Gestion', default=True)
registro = st.Page("pages/registro.py", title= 'Registro')

navegacion = st.navigation(
    [gestion, registro]
)

navegacion.run()