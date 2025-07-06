import streamlit as st
import pandas as pd
import joblib

# Load model and scaler
model = joblib.load("outputs/xgb_truck_model.pkl")
scaler = joblib.load("outputs/scaler.pkl")

st.set_page_config(page_title="🚛 Mining Truck Failure Prediction", layout="centered")
st.title("🚛 Mining Truck Failure Prediction")

st.sidebar.header("Sensor Inputs")
engine_temp = st.sidebar.slider("Engine Temperature (°C)", 60, 150, 90)
vibration_level = st.sidebar.slider("Vibration Level", 0, 100, 30)
oil_pressure = st.sidebar.slider("Oil Pressure (psi)", 10, 100, 60)
load_weight = st.sidebar.slider("Load Weight (tons)", 10, 200, 100)
RPM = st.sidebar.slider("RPM", 1000, 4000, 2200)
last_maintenance_days = st.sidebar.slider("Days Since Last Maintenance", 0, 60, 20)

if st.button("🔍 Predict Failure"):
    input_df = pd.DataFrame([[
        engine_temp, vibration_level, oil_pressure,
        load_weight, RPM, last_maintenance_days
    ]], columns=[
        "engine_temp", "vibration_level", "oil_pressure",
        "load_weight", "RPM", "last_maintenance_days"
    ])
    input_scaled = scaler.transform(input_df)
    prediction = model.predict(input_scaled)[0]
    prob = model.predict_proba(input_scaled)[0][1]

    if prediction == 1:
        st.error(f"⚠️ High Failure Risk! Probability: {prob:.2f}")
    else:
        st.success(f"✅ Truck is Safe. Failure Risk: {prob:.2f}")
