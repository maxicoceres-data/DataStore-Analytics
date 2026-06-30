import pandas as pd 
import sqlite3
from pathlib import Path


DIR_PATH = Path(__file__).parent.parent
DATA_PATH = DIR_PATH / "database" / "database.db"

def run_query(query):
    conn = sqlite3.connect(DATA_PATH)
    
    df = pd.read_sql(query,conn)

    conn.close()
    return df




def total_venta():
    query = "SELECT ROUND(SUM(total_venta), 2) AS ventas_totales FROM ventas;"
    
    return query


def ticket_promedio():
    query = "SELECT ROUND(AVG(total_venta), 2) AS ticket_promedio FROM ventas;"
    
    return query


def top_5_prod_facturados():
    query = """SELECT producto,
ROUND(SUM(total_venta), 2) AS facturación
FROM ventas
GROUP BY producto
ORDER BY facturación DESC
LIMIT 5;"""
    
    return query



def facturacion_categoria():
    query = """SELECT categoria,
    ROUND(SUM(total_venta), 2) AS facturación
FROM ventas
GROUP BY categoria
ORDER BY facturación DESC;"""
    
    return query



def facturacion_canal():
    query = """SELECT canal,
    ROUND(SUM(total_venta), 2) AS facturación
FROM ventas
GROUP BY canal
ORDER BY facturación DESC;"""
    
    return query



def ventas_mes():
    query = """SELECT strftime('%Y-%m', fecha) as mes,
    ROUND(SUM(total_venta), 2) AS facturación
FROM ventas
GROUP BY mes
ORDER BY mes ASC;"""
    
    return query


def ventas_dia_semana():
    query = """SELECT CASE
        strftime('%w', fecha)
        WHEN '0' THEN 'Domingo'
        WHEN '1' THEN 'Lunes'
        WHEN '2' THEN 'Martes'
        WHEN '3' THEN 'Miercoles'
        WHEN '4' THEN 'Jueves'
        WHEN '5' THEN 'Viernes'
        WHEN '6' THEN 'Sábado'
    END as dia_semana,
    ROUND(SUM(total_venta), 2) AS facturación
FROM ventas
GROUP BY dia_semana
ORDER BY facturación DESC;"""
    
    return query



def cantidad_ordenes():
    query = """SELECT strftime('%Y-%m', fecha) AS mes,
    COUNT(DISTINCT id_orden) AS cantidad_ordenes
FROM ventas
GROUP BY mes
ORDER BY mes ASC;"""
    
    return query






resultado_total_venta = run_query(total_venta())
resultado_ticket_promedio = run_query(ticket_promedio())
resultado_top_5 = run_query(top_5_prod_facturados())
resultado_facturacion_categoria = run_query(facturacion_categoria())
resultado_facturacion_canal = run_query(facturacion_canal())
resultado_venta_mes = run_query(ventas_mes())
resultado_dia_semana = run_query(ventas_dia_semana())
resultado_cantidad_ordenes = run_query(cantidad_ordenes())


