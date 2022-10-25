import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

plt.style.use('seaborn')

st.title('California Housing Data (1990) by Vanessa')

st.subheader('See more filters in the sidebar:')

df = pd.read_csv('housing.csv')

HousePrice_filter = st.slider('Median House Price',0.0,500001.0,200000.0)
df = df[df.median_house_value <= HousePrice_filter]

location_filter = st.sidebar.multiselect(
     'Choose the location type',
     ['NEAR BAY', '<1H OCEAN', 'INLAND', 'NEAR OCEAN', 'ISLAND'],
     ['NEAR BAY', '<1H OCEAN', 'INLAND', 'NEAR OCEAN', 'ISLAND'])  
df = df[df['ocean_proximity'].isin(location_filter)]

level = st.sidebar.radio(
    "Choose income level",
    ('Low', 'Medium', 'High'))

if level == 'Low':
    df = df[df.median_income <= 2.5]
elif level == 'High':
    df = df[df.median_income >= 4.5]
else:
    df = df[(df.median_income < 4.5) & (df.median_income > 2.5)]
    


st.map(df)
fig, ax = plt.subplots()
st.subheader('Histogram of the Median House Value')
a = df.median_house_value.hist(bins=30)
st.pyplot(fig)
