import streamlit as st



st.title("Practice Streamlit")
st.header("Ilove MAth")

st.subheader("Personal info")



first_name = st.text_input('first name')
last_name = st.text_input('Last Name')

major = st.selectbox('What is your major', 
                     ["","CS", "IT", "Math", "DS"])
