import streamlit as st
import joblib
import numpy as np
from sklearn.preprocessing import StandardScaler

st.title("Student Stress Level Prediction")
st.write("Instructions: Please input your daily hours for various activities. Ensure that the total does not exceed 24 hours and should be exactly 24 hours.")

if 'total_hours' not in st.session_state:
    st.session_state.total_hours = 0

def validate_total_hours(new_value, current_total):
    return current_total + new_value <= 24

Study_Hours_Per_Day = st.number_input(
    "Study Hours per Day", 
    min_value=0.0, 
    max_value=24.0, 
    value=2.0, 
    step=0.1
)

Extracurricular_Hours_Per_Day = st.number_input(
    "Extracurricular Activities per Day",
    min_value=0.0,
    max_value=20.0,
    value=3.0,
    step=0.1
)

Sleep_Hours_Per_Day = st.number_input(
    "Sleep Hours per Day",
    min_value=0.0,
    max_value=24.0,
    value=6.0,
    step=0.1
)

Social_Hours_Per_Day = st.number_input(
    "Social Hours per Day",
    min_value=0.0,
    max_value=24.0,
    value=1.0,
    step=0.1
)

Physical_Activity_Hours_Per_Day = st.number_input(
    "Physical Activity Hours per Day",
    min_value=0.0,
    max_value=24.0,
    value=5.0,
    step=0.1
)

total_hours = (Study_Hours_Per_Day + Extracurricular_Hours_Per_Day + 
               Sleep_Hours_Per_Day + Social_Hours_Per_Day + 
               Physical_Activity_Hours_Per_Day)

st.write(f"Total hours: {total_hours:.1f}/24")

GPA = st.number_input("GPA (0.0 - 4.0)", min_value=0.0, max_value=4.0, value=3.0, step=0.1)

if abs(total_hours - 24.0) < 0.01:
    predict_button = st.button('Predict Stress Level')
    if predict_button:
        # Load the model, scaler and columns
        model_data = joblib.load('Model/svm_model.pkl')
        model = model_data['model']
        scaler = model_data['scaler']
        columns = model_data['columns']
        
        # Prepare input data
        input_data = [[Study_Hours_Per_Day, Extracurricular_Hours_Per_Day, Sleep_Hours_Per_Day, 
            Social_Hours_Per_Day, Physical_Activity_Hours_Per_Day, GPA]]
        
        # Scale the input data
        scaled_data = scaler.transform(input_data)
        
        # Make prediction
        prediction = model.predict(scaled_data)[0]
        
        # Map prediction to stress level
        stress_map = {0: "High", 1: "Low", 2: "Moderate"}
        stress_level = stress_map[prediction]
        
        if stress_level == "High":
            st.error(f"Stress Level: {stress_level}")
        elif stress_level == "Moderate":
            st.warning(f"Stress Level: {stress_level}")
        else:
            st.success(f"Stress Level: {stress_level}")

else:
    remaining = 24.0 - total_hours
    st.warning(f"Please allocate {remaining:.1f} more hours to complete your 24-hour schedule")


