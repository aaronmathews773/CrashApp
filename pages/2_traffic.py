import streamlit as st
import pandas as pd

st.title('Traffic Data in San Jose')

st.write('Just like how analyzing crash data can help prevent collisions, analyzing traffic data can hopefully lead to less traffic congestion. This could happen in terms of better road design, introduction of more buses, or something else.')

st.write('Note: only 1,000 values were used to allow for better performance')

data = pd.read_csv('Average_Daily_Traffic.csv')
truncated_data = data.head(1000)

st.map(truncated_data)

st.write(truncated_data)

st.write('Try out the slider below to see the average daily traffic counts in various intersections')
street = st.select_slider('Slide to the intersection you want to analyze', truncated_data['NEARINTERS'])
st.write(f':green[{truncated_data[truncated_data["NEARINTERS"] == street]["ADT"]}]')