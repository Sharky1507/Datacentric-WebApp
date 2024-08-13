import streamlit as st
import pandas as pd
import numpy as np





def lat_lon_conversion(dataFile):
    #Do some more processing. This function takes a lat-long list and separates lat and Lon of each trip
    df=pd.read_csv(dataFile)
    n=20
    df = df.head(n) 

    #Convert string to list
    df['polyline'] = df['polyline'].apply(eval)

    count=0
    #Now tuples are being identified and iterated well
    for i in (df['polyline']):
        list_lat=[]
        list_lon=[]

        # i is list
        for x in i:
            #x is a tuple, x[0] and x[1] are elements
            list_lat.append(x[0])
            list_lon.append(x[1])
        df['polyline_lat'][count]=list_lat
        df['polyline_lon'][count]=list_lon
        count=count+1
    
    #Display the dataframe
    st.subheader("Dataset Prepared for the Application:")
    return df

    
