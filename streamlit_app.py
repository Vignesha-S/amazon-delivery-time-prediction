# streamlit_app.py
import streamlit as st
import pandas as pd
import numpy as np
import joblib
from datetime import datetime

# -----------------------------------------------------------
# Load the trained model
# -----------------------------------------------------------
model = joblib.load("xgb_delivery_time.pkl")

# -----------------------------------------------------------
# Page settings
# -----------------------------------------------------------
st.set_page_config(page_title="Amazon Delivery Time Predictor", layout="centered")

st.title("📦 Amazon Delivery Time Prediction")
st.markdown("Enter the order details to predict the **expected delivery time (in minutes)**.")

# -----------------------------------------------------------
# User Inputs
# -----------------------------------------------------------

st.header("Order Details")

# Numeric inputs
distance_km = st.number_input("Distance (km)", min_value=0.0, value=5.0, step=0.5)
prep_time_min = st.number_input("Preparation Time (minutes)", min_value=0.0, value=15.0, step=1.0)
agent_age = st.number_input("Delivery Agent Age", min_value=18, max_value=70, value=30, step=1)
agent_rating = st.slider("Delivery Agent Rating", min_value=1.0, max_value=5.0, value=4.5, step=0.1)

# Time-based inputs
order_hour = st.slider("Order Hour (0-23)", min_value=0, max_value=23, value=14, step=1)
order_dayofweek = st.selectbox(
    "Day of Week",
    options=[0,1,2,3,4,5,6],
    format_func=lambda x: ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"][x]
)

# Categorical inputs
traffic_choice = st.selectbox(
    "Traffic Condition",
    options=["low","medium","high","jam"]
)

weather_choice = st.selectbox(
    "Weather Condition",
    options=["sunny","fog","sandstorms","stormy","windy"]
)

# -----------------------------------------------------------
# Build feature vector matching training data
# -----------------------------------------------------------

# Initialize all columns with 0
input_dict = {
    'Distance_km': distance_km,
    'Order_Hour': order_hour,
    'Order_DayOfWeek': order_dayofweek,
    'Prep_Time_Min': prep_time_min,
    'Agent_Age': agent_age,
    'Agent_Rating': agent_rating,
    'Weather_fog': 0,
    'Weather_sandstorms': 0,
    'Weather_stormy': 0,
    'Weather_sunny': 0,
    'Weather_windy': 0,
    'Traffic_jam': 0,
    'Traffic_low': 0,
    'Traffic_medium': 0,
    'Traffic_nan': 0
}

# Set chosen weather and traffic
weather_col = f"Weather_{weather_choice}"
if weather_col in input_dict:
    input_dict[weather_col] = 1

traffic_col = f"Traffic_{traffic_choice}"
if traffic_col in input_dict:
    input_dict[traffic_col] = 1

# Convert to DataFrame
input_data = pd.DataFrame([input_dict])

st.markdown("### 📝 Feature Vector Preview")
st.dataframe(input_data)

# -----------------------------------------------------------
# Prediction
# -----------------------------------------------------------
if st.button("🚀 Predict Delivery Time"):
    prediction = model.predict(input_data)[0]
    st.success(f"✅ Estimated Delivery Time: **{prediction:.2f} minutes**")

# -----------------------------------------------------------
# Footer
# -----------------------------------------------------------
st.markdown("---")
st.markdown("Developed with ❤️ by Vignesha S")
