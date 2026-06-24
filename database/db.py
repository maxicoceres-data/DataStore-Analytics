import pandas as pd 
import sqlite3

df = pd.read_csv("ventas_datastore.csv")

conn = sqlite3.connect("database.db")

df.to_sql('ventas', conn, if_exists="replace", index=False)

conn.close()

