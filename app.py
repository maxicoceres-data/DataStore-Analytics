import streamlit as st 
import pandas as pd
from utils.data_loader import get_data


df = get_data()

st.dataframe(df)

st.write(df.columns)