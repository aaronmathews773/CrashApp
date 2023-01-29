import streamlit as st
import requests
import json

st.map()

lattitude1 = 30.60
lattitude2 = 30.64
longitude1 = 96.30
longitude2 = 96.34

begin_date = '2022-10-11'
end_date = '2022-11-11'

methane_url = f'https://api.v2.emissions-api.org/api/v2/methane/statistics.json?geoframe={longitude1-1}&geoframe={lattitude1-1}&geoframe={longitude2+1}&geoframe={lattitude2+1}&interval=day&begin={begin_date}&end={end_date}&limit=100&offset=0'
carbon_monoxide_url = f'https://api.v2.emissions-api.org/api/v2/carbonmonoxide/statistics.json?geoframe={longitude1-1}&geoframe={lattitude1-1}&geoframe={longitude2+1}&geoframe={lattitude2+1}&interval=day&begin={begin_date}&end={end_date}&limit=100&offset=0'
ozone_url = f'https://api.v2.emissions-api.org/api/v2/ozone/statistics.json?geoframe={longitude1-1}&geoframe={lattitude1-1}&geoframe={longitude2+1}&geoframe={lattitude2+1}&interval=day&begin={begin_date}&end={end_date}&limit=100&offset=0'
nitrogen_dioxide_url = f'https://api.v2.emissions-api.org/api/v2/nitrogendioxide/statistics.json?geoframe={longitude1-1}&geoframe={lattitude1-1}&geoframe={longitude2+1}&geoframe={lattitude2+1}&interval=day&begin={begin_date}&end={end_date}&limit=100&offset=0'

methane_object = requests.get(methane_url).json()
carbon_monoxide_object = requests.get(carbon_monoxide_url).json()
ozone_object = requests.get(ozone_url).json()
nitrogen_dioxide_object = requests.get(nitrogen_dioxide_url).json()

st.write(methane_object)

methane_avg = methane_object['value']['average']
carbon_monoxide_avg = carbon_monoxide_object['value']['average']
ozone_avg = ozone_object['value']['average']
nitrogen_dixoide_avg = nitrogen_dioxide_object['value']['average']


st.write('In the interval {begin_date} to {end_date}, the following are the averages for methane, carbon monoxide, ozone, and nitrogen in your area')




st.write('Methane Average: {methane_avg}')

st.write('Carbon Monoxide Average: {carbon_monoxide_avg}')

st.write('Ozone Average: {ozone_avg}')

st.write('Nitrogen Dioxide Average: {nitrogen_dioxide_avg}')

