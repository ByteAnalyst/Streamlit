import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns

st.title('World Cup Matches')

# load the file 
df = pd.read_csv('WorldCupMatches.csv')
st.write(df)
df.shape

# A side bar
st.sidebar.title('Select Year')
years = df['Year'].unique()
st.sidebar._selectbox('label', options=years)