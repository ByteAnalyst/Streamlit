import streamlit as st
import pandas as pd 
import numpy as np
import time

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


left_column, right_column = st.columns([1, 3])

with left_column:
    chosen = st.radio('sorted_hat',
    ("Gryffindor", "Ravenclaw", "Hufflepuff", "Slytherin"))

import streamlit as st
import time

'Starting a long computation...'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
  # Update the progress bar with each iteration.
  latest_iteration.text(f'Iteration {i+1}')
  bar.progress(i + 1)
  time.sleep(0.1)

'...and now we\'re done!'