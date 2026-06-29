import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))

import pandas as pd 
import sqlite3
from pathlib import Path
from utils.cleaning import limpieza_total

DIR_PATH = Path(__file__).parent 

df_crudo = pd.read_csv(DIR_PATH / "ventas_datastore.csv")

df_limpio, reporte = limpieza_total(df_crudo)
print(reporte)
conn = sqlite3.connect(DIR_PATH / "database.db")

df_limpio.to_sql('ventas', conn, if_exists="replace", index=False)

conn.close()
