import streamlit as st
import pandas as pd

st.title('Crash Data in San Jose')

st.write('Finding patterns in car crash data can help innovators design safer cars. Here, we look at some car crash data from the city of San Jose. We used San Jose because the data was publicly available and easy to work with.')

data = pd.read_csv('crashdata2011-2020.csv')
truncated_data = data.head(3000)

st.write('First, we can look at the 5 most common causes for car crashes')
most_common_collision_factors = truncated_data['PrimaryCollisionFactor'].value_counts().head(5)
st.write(most_common_collision_factors)
st.caption('Note: Only 3,000 values were used from the data frame to allow for better performance')
st.bar_chart(most_common_collision_factors)
st.write('The result seems straightforward enough, one would expect most car crashes to be between two vehicles.')


st.write('The weather can be another topic of interest')
most_common_crash_weather = truncated_data['Weather'].value_counts()
st.write(most_common_crash_weather)

st.bar_chart(most_common_crash_weather)

st.write('Most would expect rainy to be the most common crash weather but the data shows that clear weather was most common. This could be due to a variety of factors including that San Jose is rarely rainy. Maybe drivers also become overconfident when conditions are better than average.')

st.write('We can also look at the lighting')
most_common_lighting = truncated_data['Lighting'].value_counts()
st.write(most_common_lighting)

st.bar_chart(most_common_lighting)