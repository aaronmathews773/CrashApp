import streamlit as st
import pandas as pd

st.title('Crash Data in San Jose')

st.write('Finding patterns in car crash data can help innovators design safer cars. Here, we look at some car crash data from the city of San Jose from 2011-2020. We used San Jose because the data was publicly available and easy to work with. Also, note only 3,000 values were used from the dataset to allow better performance.')

data = pd.read_csv('crashdata2011-2020.csv')
truncated_data = data.head(3000)

st.header(':blue[Collision Factor]')
most_common_collision_factors = truncated_data['PrimaryCollisionFactor'].value_counts().head(5)
st.bar_chart(most_common_collision_factors)
st.write(most_common_collision_factors)
st.write('The result seems straightforward enough. Most collisions seem to have been between 2 vehicles.')

st.header(':blue[Weather]')
most_common_crash_weather = truncated_data['Weather'].value_counts(5)
st.bar_chart(most_common_crash_weather)
st.write(most_common_crash_weather)
st.write('This result seems a little counterintuitive. This could be due to a variety of factors including that San Jose is rarely rainy. Also, maybe drivers also become overconfident when conditions are better than average.')

st.header(':blue[Lighting]')
most_common_lighting = truncated_data['Lighting'].value_counts()
st.bar_chart(most_common_lighting)
st.write(most_common_lighting)

st.header(':blue[Try It Yourself!]')
st.write('Use the slider to try and find some patterns yourself!')
column = st.select_slider('Slide to change the column', options=truncated_data.columns)
most_common_in_column = truncated_data[column].value_counts()
st.bar_chart(most_common_in_column)
