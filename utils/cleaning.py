import pandas as pd 
from pathlib import Path 


DIR_PATH = Path(__file__).parent.parent
DATA_PATH = DIR_PATH / "database"

df = pd.read_csv(DATA_PATH / "ventas_datastore.csv")

