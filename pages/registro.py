import streamlit as st
from src.components.form_registro import render_form_registro

st.title('Registro de datos')


tab1, tab2, tab3 = st.tabs(['TUPR', 'TP', 'CAMARAS'])

with tab1:
    st.subheader('Registro de datos TUPR')
    st.write('Aquí puedes registrar los datos de TUPR.')
    render_form_registro('TUPR','servicios_taller')

with tab2:
    st.subheader('Registro de datos TP')
    st.write('Aquí puedes registrar los datos de TP.')
    render_form_registro('TP','servicios_taller')
with tab3:
    st.subheader('En desarrollo')