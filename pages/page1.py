import folium
import streamlit as st
import struct

from streamlit_folium import st_folium


latitude = 30.615242731499126
longitude = -96.34158496852066



st.number_input("latitude", latitude)
st.number_input("longitude", longitude)

# Display map
m = folium.Map(location=[latitude, longitude], zoom_start=16)
folium.Marker(
    [latitude, longitude], popup="Current Location", tooltip="Current Location"
).add_to(m)

# call to render Folium map in Streamlit
st_data = st_folium(m, width=725)
