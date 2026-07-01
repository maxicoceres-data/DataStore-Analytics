import streamlit as st 
import json
from pathlib import Path
from utils.metrics import resultado_total_venta, resultado_ticket_promedio
from utils.charts import figura_top_5, figura_categoria, figura_canal, figura_mes, figura_ordenes, figura_dia_semana

reporte = json.loads((Path("database/reporte.json")).read_text(encoding="utf-8"))

#metrica de streamlit
st.title("DataStore Analytics")
#mtricas de venta totales y ticket promedio (tarjeta basica)
col1, col2 = st.columns(2)
with col1:
    st.metric("Ventas totales", resultado_total_venta.iloc[0,0],border=True)
with col2:
    st.metric("Ticket Promedio", resultado_ticket_promedio.iloc[0,0],border=True)
    

st.divider()
#grafico de barras para top 5 productos facturados
figura_top_5()

st.divider()
col3,col4 = st.columns(2)
with col3:
    #grafico de barras para facuracion por categoria.
    figura_categoria()
    
with col4:
    #grafico de barras para facuracion por canal.
    figura_canal()
    
    
st.divider()

col5,col6 = st.columns(2)

with col5:
    #grafico de factuación por mes
    figura_mes()

with col6:
    figura_ordenes()

st.divider()

figura_dia_semana()


with st.expander("📋 Reporte de calidad de datos"):
    for clave, mensaje in reporte.items():
        st.write(f"**{clave}**: {mensaje}")