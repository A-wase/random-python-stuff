# Paste in terminal: streamlit run streamlit_test.py
import streamlit as st

st.title("Data Dashboard") # Create a title
st.write("Hello, World!") # Create text

import pandas as pd
# Create a simple DataFrame
data = {
    'Name': ['Spongebob', 'Patrick', 'Squidward', 'Sandy'],
    'Age': [24, 27, 22, 32],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']
}
df = pd.DataFrame(data)
st.dataframe(df)