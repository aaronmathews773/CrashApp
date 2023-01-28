import folium
import streamlit as st

from streamlit_folium import st_folium


latitude = 30.6152
longitude = -96.3415

st.text_input(latitude)
st.text_input(longitude)

# Display map
m = folium.Map(location=[latitude, longitude], zoom_start=16)
folium.Marker(
    [latitude, longitude], popup="Current Location", tooltip="Current Location"
).add_to(m)

# call to render Folium map in Streamlit
st_data = st_folium(m, width=725)
