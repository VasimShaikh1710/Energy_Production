import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import pickle

# Load the trained model
pickle_in = open("RFRegressor.pkl", 'rb')
RFR = pickle.load(pickle_in)

# Function to make predictions
def Ene_prediction(Temperature, exhaust_vacuum, amb_pressure, r_humidity):
    prediction = RFR.predict([[Temperature, exhaust_vacuum, amb_pressure, r_humidity]])
    return prediction[0]

# Streamlit UI
st.header("Energy Production Prediction")

# Input sliders
with st.form("Form 2"):
    Temperature = st.slider("Temperature", min_value=1, max_value=40)
    exhaust_vacuum = st.slider("Exhaust Vacuum", min_value=25, max_value=85)
    amb_pressure = st.slider("Ambient Pressure", min_value=900, max_value=1035)
    r_humidity = st.slider("Relative Humidity", min_value=30, max_value=101)
    st.form_submit_button("Predict")
    if st.form_submit_button:
        result = Ene_prediction(Temperature, exhaust_vacuum, amb_pressure, r_humidity)
        st.success(f"Predicted Energy Production: {(result).round(2)}")

# Visualization
st.header("Visualization")

df = pd.DataFrame({
    "Temperature": [Temperature],
    "Exhaust Vacuum": [exhaust_vacuum],
    "Ambient Pressure": [amb_pressure],
    "Relative Humidity": [r_humidity],
    "Energy_pred" : [result]
})
st.write(df)

