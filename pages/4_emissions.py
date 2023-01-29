import streamlit as st
import requests
import pandas as pd



st.title('View Emissions Data in Your Location')

st.write('Enter your longitude and lattitude to view emissions data in your location')

if 'longitude' not in st.session_state:
    st.session_state.longitude = -96.3344

if 'latitude' not in st.session_state:
    st.session_state.lattitude = 30.6280

st.session_state.longitude = float(st.text_input('Longitude', -96.3344))
st.session_state.lattitude = float(st.text_input('Lattitude', 30.6280))

coordinates = pd.DataFrame.from_dict({'lon':[st.session_state.longitude], 'lat':[st.session_state.lattitude]})

st.map(coordinates)


begin_date = st.text_input('Beginning Date', '2022-10-11')
end_date = st.text_input('End Date', '2022-11-11')

# Request urls to view averages of each chemical
methane_url = f'https://api.v2.emissions-api.org/api/v2/methane/statistics.json?geoframe={st.session_state.longitude-2}&geoframe={st.session_state.lattitude-2}&geoframe={st.session_state.longitude+2}&geoframe={st.session_state.lattitude+2}&interval=day&begin={begin_date}&end={end_date}&limit=100&offset=0'
carbon_monoxide_url = f'https://api.v2.emissions-api.org/api/v2/carbonmonoxide/statistics.json?geoframe={st.session_state.longitude-2}&geoframe={st.session_state.lattitude-2}&geoframe={st.session_state.longitude+2}&geoframe={st.session_state.lattitude+2}&interval=day&begin={begin_date}&end={end_date}&limit=100&offset=0'
ozone_url = f'https://api.v2.emissions-api.org/api/v2/ozone/statistics.json?geoframe={st.session_state.longitude-2}&geoframe={st.session_state.lattitude-2}&geoframe={st.session_state.longitude+2}&geoframe={st.session_state.lattitude+2}&interval=day&begin={begin_date}&end={end_date}&limit=100&offset=0'
nitrogen_dioxide_url = f'https://api.v2.emissions-api.org/api/v2/nitrogendioxide/statistics.json?geoframe={st.session_state.longitude-2}&geoframe={st.session_state.lattitude-2}&geoframe={st.session_state.longitude+2}&geoframe={st.session_state.lattitude+2}&interval=day&begin={begin_date}&end={end_date}&limit=100&offset=0'

methane_object = requests.get(methane_url).json()
carbon_monoxide_object = requests.get(carbon_monoxide_url).json()
ozone_object = requests.get(ozone_url).json()
nitrogen_dioxide_object = requests.get(nitrogen_dioxide_url).json()

# These lists store the daily averages of each chemical 
methane_avgs_list = [methane_object[i]['value']['average'] for i in range(len(methane_object))]
carbon_monoxide_avgs_list = [carbon_monoxide_object[i]['value']['average'] for i in range(len(carbon_monoxide_object))]
ozone_avgs_list = [ozone_object[i]['value']['average'] for i in range(len(ozone_object))]
nitrogen_dioxide_avgs_list = [nitrogen_dioxide_object[i]['value']['average'] for i in range(len(nitrogen_dioxide_object))]


# Since the data is not complete, methane has less data points than carbon monoxide and there are some other lenght differences as well. Therefore, multiple charts were made
st.line_chart(pd.DataFrame({'methane': methane_avgs_list}))
st.line_chart(pd.DataFrame({'carbon monoxide': carbon_monoxide_avgs_list}))
st.line_chart(pd.DataFrame({'ozone': ozone_avgs_list}))
st.line_chart(pd.DataFrame({'nitrogen dioxide': nitrogen_dioxide_avgs_list}))

