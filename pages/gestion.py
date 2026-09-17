import streamlit as st
from src.components.table_info import render_table_info

st.title('Gestion Transportes')



tab1,tab2,tab3 = st.tabs(['TUPR', 'TP', 'CAMARAS'])

with tab1:
    render_table_info('TUPR','servicios_taller')
   
with tab2:
    render_table_info('TP','servicios_taller')

with tab3:
    st.subheader('En desarrollo')