import streamlit as st 
import plotly.express as px
import pandas as pd
from utils.data_loader import get_data
from utils.metrics import resultado_cantidad_ordenes,resultado_dia_semana, resultado_facturacion_canal, resultado_facturacion_categoria,resultado_ticket_promedio,resultado_top_5,resultado_total_venta,resultado_venta_mes,run_query



def figura_top_5():
    group_label_top_5 = ["producto","facturación"]
    fig_top_5 = px.bar(resultado_top_5,group_label_top_5[0],group_label_top_5[1], title="Top 5 Productos Facturados")

    grafico = st.plotly_chart(fig_top_5)
    
    return grafico


def figura_categoria():
    group_label_categoria = ["categoria","facturación"]
    fig_categoria =  px.pie(resultado_facturacion_categoria,names=group_label_categoria[0], values=group_label_categoria[1], title="Faturación por Categoría")
    grafico = st.plotly_chart(fig_categoria)
    
    return grafico


def figura_canal():
    group_label_canal = ["canal","facturación"]
    fig_canal =  px.pie(resultado_facturacion_canal,names=group_label_canal[0], values=group_label_canal[1], title="Faturación por Canal")
    grafico = st.plotly_chart(fig_canal)
    
    return grafico


def figura_mes():
    group_label_mes = ["mes","facturación"]
    fig_mes = px.line(resultado_venta_mes,x=group_label_mes[0], y=group_label_mes[1],title="Facturación por mes")
    grafico = st.plotly_chart(fig_mes)
    
    return grafico


def figura_ordenes():
    group_label_cantidad_ord = ["mes","cantidad_ordenes"]
    fig_cantidad = px.line(resultado_cantidad_ordenes, x=group_label_cantidad_ord[0], y=group_label_cantidad_ord[1], title="Cantidad de ordenes por mes")
    grafico = st.plotly_chart(fig_cantidad)
    
    return grafico


def figura_dia_semana():
    group_dia = ["dia_semana","facturación"]
    fig_dia_semana = px.bar(resultado_dia_semana, x=group_dia[0], y=group_dia[1], title="Facturación por dia de semana")
    grafico = st.plotly_chart(fig_dia_semana)
    
    return grafico