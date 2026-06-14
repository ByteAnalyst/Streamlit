import streamlit as st
import pandas as pd 
import numpy as np

chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns= ['a', 'b', 'c'])

st.line_chart(chart_data)

# using st.map

map_data = pd.DataFrame(
    np.random.randn(1000, 2) / (50, 50) + [33.768, 72.361],
    columns= ['lat', 'lon']
)
st.map(map_data)


# Widgets

if st.button('click me!'):
    st.write('you clicked')

if st.checkbox('checked'):
    st.write(map_data)

age = st.slider('Pick a number', min_value=0, max_value=100, value= 25)
st.write('You picked', age)

city = st.selectbox('Pick a city', ['Lahore', 'Karachi', 'Islamabad'])
st.write('You picked:', city)


# using st.session_state
st.sidebar.text_input('Your name', key='name')
st.write('Hello', st.session_state.name)