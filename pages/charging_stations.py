#!/usr/bin/env python3
import streamlit as st
import requests
import json
import pandas as pd

r = requests.get('https://developer.nrel.gov/api/alt-fuel-stations/v1/nearest.json?latitude=30&longitude=-96&radius=200&api_key=tc7h97D0XpIlz2axGxYBudN49ZaSn9NUnYDur3OP').text

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
