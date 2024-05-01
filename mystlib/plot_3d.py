import pandas as pd
import numpy as np
import plotly.express as px
import streamlit as st
import pydeck as pdk
def run(df):
    st.subheader('Plot 01: ')
    fig1 = px.scatter_3d(df,
    x = 'passenger_count',
    y = 'distance',
    z= 'duration',
    title= "Relation between Passenger, Distance and Duration",
    color = 'passenger_count',
    width = 800,
    height = 600,


    )
    st.plotly_chart(fig1)
    #plot no 2
    st.subheader("Plot no 2")
    df = df.explode(['polyline_lat','polyline_lon'], ignore_index = True)
    view = pdk.data_utils.compute_view(df[['polyline_lon','polyline_lat']])
    view.pitch = 70
    view.bearing = 60
    view.latitude = df['polyline_lat'].iloc[-1]
    view.longitude = df['polyline_lon'].iloc[-1]
    view.zoom = 8
    view.min_zoom = 3
    view.max_zoom = 30

    layer = pdk.Layer(
        'HexagonLayer',
        df,
        get_position = ['polyline_lon','polyline_lat'],
        auto_highlight = True,
        elevation_scale = 50,
        get_radius = 5,
        pickable=True,
        extruded = True,
        elevation_range = [0,3000],
        coverage = 1,
        getTextAnchor = '"middle"',
        get_alignment_baseline = '"bottom"'

    )
    tooltip = {
        "html": "No. of Rides take from here: {elevationValue}"
    }
    final = pdk.Deck(
        layers = [layer],
        initial_view_state = view,
        tooltip = tooltip

    )
    st.pydeck_chart(final) 

