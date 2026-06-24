import pandas as pd 
import sqlite3
from pathlib import Path

DIR_PATH = Path(__file__).parent 

df = pd.read_csv(DIR_PATH / "ventas_datastore.csv")

conn = sqlite3.connect(DIR_PATH / "database.db")

df.to_sql('ventas', conn, if_exists="replace", index=False)

conn.close()
