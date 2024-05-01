import pandas as pd
import streamlit as st
def run(df):
    st.title("Single-column Selection")
    col=st.selectbox('Select one column: ', df.columns)
    st.write("You selected: ",col)
    st.write(df[col].unique())
    st.title("Multi-column Selection")
    cols = st.multiselect("Select Many columns",df.columns,default = [])
    st.write("You selected: ", cols)
    st.write(df[cols])

