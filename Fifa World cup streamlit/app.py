import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns

st.title('World Cup Matches')

# load the file 
df = pd.read_csv('WorldCupMatches.csv')

# Data cleaning
df = df.fillna(0)
df = df.drop_duplicates()
df.reset_index(drop=True, inplace=True)


df['Year'] = df['Year'].astype(int)
df['Attendance'] = df['Attendance'].astype(int)


# A side bar
st.sidebar.title('Select Year')
years = df['Year'].unique()
selected_year = st.sidebar.selectbox('label', options=years)

st.sidebar.title('Select Stage')
stages = df['Stage'].unique()
selected_stage = st.sidebar.selectbox('label', options=stages)

filtered_df = df[(df['Year'] == selected_year) & (df['Stage'] == selected_stage)]

show_data = st.checkbox('Show Raw Data')

if show_data:
    st.write(filtered_df)


col1, col2, col3 = st.columns(3)

col1.metric('Total Matches', len(filtered_df))
col2.metric('Total Home Team Goals', int(filtered_df['Home Team Goals'].sum()))
col3.metric('Total Away Team Goals', int(filtered_df['Away Team Goals'].sum()))


# Adding a chart for home team goals 
st.subheader('Home Team Goals By Stage')
st.bar_chart(data=filtered_df, x= 'Stage', y= 'Home Team Goals')


# Adding a chart for away team goals
st.subheader('Away Team Goals By Stage')
st.bar_chart(data=filtered_df, x= 'Stage', y= 'Away Team Goals')

# Adding a chart for Attendance
st.subheader('Attendance By Stage')
st.bar_chart(data=filtered_df, x= 'Stage', y= 'Attendance')