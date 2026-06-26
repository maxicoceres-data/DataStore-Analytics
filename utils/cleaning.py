import pandas as pd 


#funcion de limpieza de precio

def limpieza_precio(df):
    """Limpieza de precio.

    Args:
        df (_type_): dataframe subido por cliente
        reporte (_type_): pequeño reporte de cantidad limpiada.

    Returns:
        Retorna el dataframe y el reporte.
    """
    precios_negativos = df[df["precio_unitario"] <= 0]
    filas_precios_negativos = len(precios_negativos)
    filas_df = len(df)
    
    if filas_precios_negativos < (filas_df * 0.1):
        df = df[df["precio_unitario"] > 0].copy()
        reporte = f"Se eliminan {filas_precios_negativos} filas por precios nulos, 0 o negativos"
    else:
        reporte = f"Demasiados precios inválidos ({filas_precios_negativos} / {filas_df}). Revisar el archivo."
    return df, reporte





#funcion de cantidad

def limpieza_cantidad(df):
    cantidad_null_negativo = df.loc[(df["cantidad"]<=0) | (df["cantidad"].isna())]
    filas_cantidad_null_negativo = len(cantidad_null_negativo)
    
    if filas_cantidad_null_negativo < df.shape[0] * 0.1:
        df = df[df["cantidad"] > 0].copy()
        reporte = f"Se eliminan {filas_cantidad_null_negativo} filas por precios nulos, 0 o negativos"
    else:
        reporte = f"Cantidad erronea alta. ({df.shape[0] / filas_cantidad_null_negativo}), revisar el dataset."
        
    return df, reporte



def limpieza_fecha(df):
    
    invalidas = df["fecha"].isna() | (pd.to_datetime(df["fecha"], errors="coerce").isna())
    
    
    df["fecha"] = pd.to_datetime(df["fecha"], errors="coerce")
    n = df["fecha"].isna().sum()
    df = df[df["fecha"].notna()].copy()
    reporte = f"Se eliminan {n} filas por fecha inválida"
    return df, reporte


def limpieza_col_texto(df,columna):
    df[columna] = (
        df[columna]
        .str.strip()
        .str.replace(r"\s+", " ", regex= True)
        .str.lower()
    )
    
    productos_nulos = df[df[columna].isna()]
    
    df[columna] = df[columna].fillna("sin especificar")
    
    reporte = f"Hay {len(productos_nulos)} {columna} nulos, se modifica por 'sin especidifcar'"
    
    return df, reporte


def limpieza_total(df):
    
    df = df.copy()
    reporte = {}
    
    df.columns = df.columns.str.lower().str.strip().str.replace(" ", "_")
    
    df,reporte["precio"] = limpieza_precio(df)
    df ,reporte["producto"]= limpieza_col_texto(df,"producto")
    df ,reporte["cantidad"]= limpieza_cantidad(df)
    df ,reporte["fecha"]= limpieza_fecha(df)
    df ,reporte["metodo_pago"]= limpieza_col_texto(df,"metodo_pago")
    df ,reporte["ciudad"]= limpieza_col_texto(df,"ciudad")
    df ,reporte["canal"]= limpieza_col_texto(df,"canal")
    
    
    df = df.drop_duplicates() 

    df["total_venta"] = df["precio_unitario"] * df["cantidad"]
    
    
    return df, reporte