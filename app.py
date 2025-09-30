import streamlit as st

st.title("Stress Level Prediction")

st.write("This is a simple app to predict stress levels based on user input.")
st.write("Please enter your details below:")

Study_hours = st.number_input("Study Hours per Day", min_value=0, max_value=24, value=2)
Extracurricular_activities = st.number_input("Extracurricular Activities per Day", min_value=0, max_value=20, value=3)
Sleep_hours = st.number_input("Sleep Hours per Day", min_value=0, max_value=24, value=7)
Social_hours = st.number_input("Social Hours per Day", min_value=0, max_value=24, value=2)
Physical_activity_hours = st.number_input("Physical Activity Hours per Day", min_value=0, max_value=24, value=1)
GPA = st.number_input("GPA (0.0 - 4.0)", min_value=0.0, max_value=4.0, value=3.0, step=0.1)

