import streamlit as st
from datetime import date
import pandas as pd
import numpy as np

st.title("Practice Streamlit")
st.header("Ilove MAth")

st.subheader("Personal info")



first_name = st.text_input('first name')
last_name = st.text_input('Last Name')

major = st.selectbox('What is your major', 
                     ["","CS", "IT", "Math", "DS"])

date_started = st.date_input("Please put Date")
campuses_map = st.checkbox("FIU MAP")
if campuses_map:
  st.write("user selected the field"
           map_data = pd.DataFrame(
              np.array([
[25.759005, -80.373825],
[25.770459, -80.368130],
[25.910728, -80.138982],
[25.992332, -80.339832],
[25.763418, -80.190564],
[25.790110, -80.131561],
[24.950351, -80.452974],
[38.895549, -77.011910],
[25.772754, -80.134411],
[25.781113, -80.132460]])
columns=['lat','lon'])

st.map(map_data)
