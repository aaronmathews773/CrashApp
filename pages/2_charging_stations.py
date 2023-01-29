#!/usr/bin/env python3
import streamlit as st
import requests
import json
import pandas as pd
import apiKey

st.write("Charging Stations Near You")

if 'latitude' not in st.session_state:
    st.session_state.latitude = 30.615242731499126
    st.session_state.longitude = -96.34158496852066

def update_counter():
    st.session_state.latitude = st.session_state.update_lat
    st.session_state.longitude = st.session_state.update_lon

with st.form(key='my_form'):
    st.number_input("Enter Latitude", value=0, key='update_lat')
    st.number_input("Enter Longitude", value=0, key='update_lon')
    submit = st.form_submit_button(label='Update', on_click=update_counter)

st.write("Current Latitude: ", st.session_state.latitude)
st.write("Current Longitude: ", st.session_state.longitude)

r = requests.get(f'https://developer.nrel.gov/api/alt-fuel-stations/v1/nearest.json?latitude={st.session_state.latitude}&longitude={st.session_state.longitude}&radius=200&api_key={apiKey.chargingStation}').text

data = json.loads(r)
#st.write(data["fuel_stations"])

latitudes = []
longitudes = []

for station in data["fuel_stations"]:
    latitudes.append(station["latitude"])
    longitudes.append(station["longitude"])

coordinates = pd.DataFrame({'lat': latitudes, 'lon': longitudes})

st.map(coordinates)
#locations = json.loads(r)
