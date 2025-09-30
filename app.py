import streamlit as st
import joblib
import numpy as np
from sklearn.preprocessing import StandardScaler

# Load only the trained model
MODEL_PATH = 'D:/Codes/Stress-Level-Prediction/Model/svm_model.joblib'


try:
    model = joblib.load(MODEL_PATH)

except FileNotFoundError:
    st.error("Error: Model file not found. Please check if the file exists in the correct location.")
    st.stop()

st.title("Stress Level Prediction")

st.write("This is a simple app to predict stress levels based on user input.")
st.write("Please enter your details below:")
st.write("")

Study_hours = st.number_input("Study Hours per Day", min_value=0, max_value=24, value=2)

Extracurricular_activities = st.number_input("Extracurricular Activities per Day", min_value=0, max_value=20, value=3)

Sleep_hours = st.number_input("Sleep Hours per Day", min_value=0, max_value=24, value=6)

Social_hours = st.number_input("Social Hours per Day", min_value=0, max_value=24, value=1)

Physical_activity_hours = st.number_input("Physical Activity Hours per Day", min_value=0, max_value=24, value=5)

GPA = st.number_input("GPA (0.0 - 4.0)", min_value=0.0, max_value=4.0, value=3.0, step=0.1)

def handle_outliers(data):
    Q1 = np.percentile(data, 25)
    Q3 = np.percentile(data, 75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    return np.clip(data, lower_bound, upper_bound)

if st.button('Predict Stress Level'):
    # Create input array
    input_data = np.array([[Study_hours, Extracurricular_activities, Sleep_hours, 
                           Social_hours, Physical_activity_hours, GPA]])
    
    # Handle outliers
    for i in range(input_data.shape[1]):
        input_data[:, i] = handle_outliers(input_data[:, i])
    
    # Create and fit StandardScaler on the input data
    scaler = StandardScaler()
    input_scaled = scaler.fit_transform(input_data)
    
    # Make prediction
    prediction = model.predict(input_scaled)[0]
    
    # Map prediction to stress level
    stress_levels = {0: "High", 1: "Low", 2: "Moderate"}
    result = stress_levels[prediction]
    
    st.write(f"You may have a **{result}** stress level")
    
    # Add some color coding for the result
    if result == "High":
        st.error("⚠️ Consider talking to a counselor or taking stress management measures")
    elif result == "Moderate":
        st.warning("⚠️ Monitor your stress levels and maintain a balanced lifestyle")
    else:
        st.success("✅ Keep maintaining your current lifestyle balance")
        