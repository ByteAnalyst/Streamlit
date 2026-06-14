import streamlit as st
import pandas as pd
import numpy as np

data_frame = pd.DataFrame(
    np.random.randn(10, 20),
    columns=('col %d' % i for i in range((20)))
)

st.dataframe(data_frame.style.highlight_max(axis=0))

st.table(data_frame)