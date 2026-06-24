import pandas as pd 
import sqlite3 
from pathlib import Path


DIR_PATH = Path(__file__).parent.parent
DATA_PATH  = DIR_PATH / "database"


def get_data():
    conn = sqlite3.connect(DATA_PATH / "database.db")
    query = ("""
             SELECT * FROM ventas
             """)
    df = pd.read_sql_query(query,conn)
    conn.close()
    return df