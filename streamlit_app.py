import pandas as pd
import plotly.express as px
import pydeck as pdk
import streamlit as st
import numpy as np
import preprocess
from mystlib import explore
from mystlib import viewonMap
from mystlib import plot_2d
from mystlib import plot_3d

st.set_page_config(layout = "wide", page_title = "Data-Centric-App",page_icon = ":taxi:")


df = preprocess.lat_lon_conversion("readydataset.csv")
message = "Select a functionality from the list below"
with st.sidebar:
    st.markdown(message)
    page = st.selectbox('Select:',
    ['View Data Using Dropdowns',
    'Visualize Data on a Map',
    '2D Charts and Histograms',
    '3D Charts and Histograms'])
st.dataframe(df)
if page == 'View Data Using Dropdowns':
    explore.run(df)
elif page == 'Visualize Data on a Map':
    viewonMap.run(df)
elif page == '2D Charts and Histograms':
    plot_2d.run(df)
else:
    plot_3d.run(df)
    