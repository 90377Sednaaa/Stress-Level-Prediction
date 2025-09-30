import streamlit as st

st.title("Stress Level Prediction")

st.write("This is a simple app to predict stress levels based on user input.")
st.write("Please enter your details below:")

st.markdown("## Study Hours per Day")
Study_hours = st.number_input("", min_value=0, max_value=24, value=2)

st.markdown("## Extracurricular Activities per Day")
Extracurricular_activities = st.number_input("", min_value=0, max_value=20, value=3)

st.markdown("## Sleep Hours per Day")
Sleep_hours = st.number_input("", min_value=0, max_value=24, value=6)

st.markdown("## Social Hours per Day")
Social_hours = st.number_input("", min_value=0, max_value=24, value=1)

st.markdown("## Physical Activity Hours per Day")
Physical_activity_hours = st.number_input("", min_value=0, max_value=24, value=5)

st.markdown("## GPA (0.0 - 4.0)")
GPA = st.number_input("", min_value=0.0, max_value=4.0, value=3.0, step=0.1)

