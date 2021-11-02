import streamlit as st
import pandas as pd
import numpy as np

"""
# Uber Pickups Excercice
"""

#DATA_URL = 'http://s3-us-west-2.amazonaws.com/streamlit-demo-data/uber-raw-data-sep14.csv.gz'
#DATA_URL = '/Users/Navas/Desktop/uber-raw-data-sep14.csv'
DATA_URL = '/Users/Navas/Desktop/uber-raw-data-sep142.csv'

@st.cache(allow_output_mutation=True)
def download_data():
    return pd.read_csv(DATA_URL)

nrow = st.sidebar.slider('No. rows to display: ', 0, 10000, value=100)
hour_range = st.sidebar.slider('Select the hour range: ', 0, 24, (8,17))

st.sidebar.write('Hours selected: ', hour_range[0], hour_range[1])

data = (download_data()
        .rename(columns={'Date/Time' : 'date_time', 'Lat' : 'lat', 'Lon' : 'lon', 'Base' : 'base'})
        .assign(date_time = lambda df: pd.to_datetime(df.date_time))
        .loc[lambda df: (df.date_time.dt.hour >= hour_range[0]) & (df.date_time.dt.hour < hour_range[1])]
        .loc[1:nrow]
)


data

st.map(data)


hist_values = np.histogram(data.date_time.dt.hour, bins=24, range=(0,24))[0]
st.bar_chart(hist_values)



