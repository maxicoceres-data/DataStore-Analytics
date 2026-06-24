import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

random.seed(42)
np.random.seed(42)

n = 5000

productos = [
    "Remera básica", "Jean slim", "Zapatillas running", "Campera impermeable",
    "Vestido floral", "Short deportivo", "Buzo hoodie", "Medias pack x3",
    "Gorra snapback", "Cinturón cuero"
]

categorias = {
    "Remera básica": "Ropa", "Jean slim": "Ropa", "Zapatillas running": "Calzado",
    "Campera impermeable": "Ropa", "Vestido floral": "Ropa", "Short deportivo": "Ropa",
    "Buzo hoodie": "Ropa", "Medias pack x3": "Accesorios",
    "Gorra snapback": "Accesorios", "Cinturón cuero": "Accesorios"
}

precios_base = {
    "Remera básica": 15000, "Jean slim": 45000, "Zapatillas running": 85000,
    "Campera impermeable": 72000, "Vestido floral": 38000, "Short deportivo": 22000,
    "Buzo hoodie": 55000, "Medias pack x3": 8000,
    "Gorra snapback": 18000, "Cinturón cuero": 25000
}

fecha_inicio = datetime(2024, 1, 1)
fechas = [fecha_inicio + timedelta(days=random.randint(0, 364)) for _ in range(n)]

productos_lista = random.choices(productos, k=n)

precios = []
for p in productos_lista:
    variacion = random.uniform(0.9, 1.1)
    precios.append(round(precios_base[p] * variacion, 2))

cantidades = np.random.randint(1, 6, size=n)

df = pd.DataFrame({
    "id_orden": range(1001, 1001 + n),
    "fecha": fechas,
    "producto": productos_lista,
    "categoria": [categorias[p] for p in productos_lista],
    "precio_unitario": precios,
    "cantidad": cantidades,
    "canal": random.choices(["MercadoLibre", "Shopify", "Tiendanube", "WooCommerce"], 
                             weights=[40, 25, 20, 15], k=n),
    "ciudad": random.choices(
        ["Buenos Aires", "Córdoba", "Rosario", "Mendoza", "Mar del Plata",
         "Santiago", "Bogotá", "Ciudad de México", "Madrid", "Lima"],
        k=n
    ),
    "metodo_pago": random.choices(
        ["Tarjeta crédito", "Tarjeta débito", "Transferencia", "Efectivo"],
        weights=[45, 25, 20, 10], k=n
    )
})

df["total_venta"] = df["precio_unitario"] * df["cantidad"]

# --- ERRORES INTENCIONALES ---

# 1. Fechas como string mal formateadas
idx_fechas_mal = random.sample(range(n), 150)
df["fecha_str"] = df["fecha"].dt.strftime("%d/%m/%Y")
for i in idx_fechas_mal:
    if random.random() >0.5:
        df.at[i, "fecha_str"] = "fecha_invalida"

# 2. Precios negativos o cero
idx_precios_mal = random.sample(range(n), 80)
for i in idx_precios_mal:
    df.at[i, "precio_unitario"] = random.choice([0, -random.uniform(100, 5000)])

# 3. Cantidades nulas o negativas
idx_cant_mal = random.sample(range(n), 60)
for i in idx_cant_mal:
    df.at[i, "cantidad"] = random.choice([0, -1, np.nan])

# 4. Filas duplicadas
duplicadas = df.sample(100)
df = pd.concat([df, duplicadas]).reset_index(drop=True)

# 5. Valores nulos en columnas clave
for col in ["producto", "canal", "ciudad", "metodo_pago"]:
    idx_nulos = random.sample(range(len(df)), 50)
    for i in idx_nulos:
        df.at[i, col] = np.nan

# 6. Productos con nombres mal escritos
idx_typos = random.sample(range(len(df)), 40)
typos = ["Remera basica", "JEAN SLIM", "zapatillas running", "campera Impermeable"]
for i in idx_typos:
    df.at[i, "producto"] = random.choice(typos)

# --- EXPORTAR ---
df.to_csv("ventas_datastore.csv", index=False)
print(f"CSV generado con {len(df)} filas")
print(f"Errores introducidos: fechas mal={len(idx_fechas_mal)}, precios mal={len(idx_precios_mal)}, duplicados=100")
    