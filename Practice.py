import streamlit as st
from datetime import data


st.title("Practice Streamlit")
st.header("Ilove MAth")

st.subheader("Personal info")



first_name = st.text_input('first name')
last_name = st.text_input('Last Name')

major = st.selectbox('What is your major', 
                     ["","CS", "IT", "Math", "DS"])

date_started = st.date_input("Please put date")
today = date.today().year
