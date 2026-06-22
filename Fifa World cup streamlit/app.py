import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns

st.title('World Cup Matches')

# load the file 
df = pd.read_csv('WorldCupMatches.csv')
st.write(df)

# Data cleaning
df = df.fillna(0)
df = df.drop_duplicates()
df.reset_index(drop=True, inplace=True)


df['Year'] = df['Year'].astype(int)
df['Attendance'] = df['Attendance'].astype(int)


# A side bar
st.sidebar.title('Select Year')
years = df['Year'].unique()
st.sidebar.selectbox('label', options=years)

total_matches = len(df)
total_goals = sum(df['Home Team Goals']) + sum(['Away Team Goals'])
total_tournaments = sum(df['Year'].unique())
st.columns(4)
