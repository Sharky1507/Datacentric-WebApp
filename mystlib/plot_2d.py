import pandas as pd
import plotly.express as px
import streamlit as st
def run(df):
    #plot 01
    st.subheader("Plot no 1: ")
    fig1= px.bar(df.groupby('passenger_count').mean(numeric_only = True), y = 'duration',title = 'Mean Travel Time for No. of Passengers')
    st.plotly_chart(fig1,use_container_width =True)
    #plot 02
    st.subheader("Plot no 2:")
    fig2 = px.scatter(df, x = 'duration', y = 'distance', title = 'Duration vs Distance Relation')
    st.plotly_chart(fig2,use_container_width= True)