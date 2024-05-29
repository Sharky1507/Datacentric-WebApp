import pandas as pd
import plotly.express as px
import streamlit as st
def run(df):
    #Enter your MapBox token here
    MAPBOX_API_KEY = st.secrets["mapbox"]["MAPBOX_API_KEY"]
    
    px.set_mapbox_access_token(MAPBOX_API_KEY)
    st.subheader("Plot 1")
    fig1 = px.scatter_mapbox(
        df,
        lat = "pickup_latitude",
        lon = "pickup_longitude",
        size = "passenger_count",
        color = "passenger_count",
        center = dict(
            lat = float(df["pickup_latitude"][0]),
            lon =float(df["pickup_longitude"][0]) 

        ),
        zoom= 10, width = 800 , height = 600


    )
    fig1.update_layout(title_text = 'Passengers in Taxi', title_x = 0.5, title_y = 1)
    st.plotly_chart(fig1,use_container_width = True)
    # second plot
    st.subheader("Plot 2: ")
    st.write("Select trip Id to Visualize")
    option = st.selectbox(' ', df["ID"])
    trip = df[df["ID"] == option]
    trip['lat'] = df['polyline_lat']
    trip['lon'] = df['polyline_lon']
    trip = trip.explode(['lat','lon'],ignore_index = True)
    fig2 = px.line_mapbox(trip,
        lat = 'lat', lon = 'lon', zoom = 10, width = 800 , height = 600
    
    )
    fig2.update_layout(title_text = "Trip Routes", title_x = 0.5, title_y = 1)
    st.plotly_chart(fig2,use_container_width=True)
