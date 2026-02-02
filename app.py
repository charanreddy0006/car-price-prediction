import streamlit as st
import pandas as pd
import joblib

# Load trained model and columns
model = joblib.load("car_price_model.pkl")
columns = joblib.load("model_columns.pkl")

st.title("🚗 Car Price Prediction System")
st.write("Enter car details and click Predict")

# User inputs
vehicle_age = st.number_input("Vehicle Age (years)", 0, 3, 5)
km_driven = st.number_input("Kilometers Driven", 0, 500000, 50000)
mileage = st.number_input("Mileage (km/l)", 5.0, 40.0, 20.0)
engine = st.number_input("Engine Capacity (CC)", 500, 5000, 1200)
max_power = st.number_input("Max Power (BHP)", 20.0, 400.0, 80.0)
seats = st.selectbox("Number of Seats", [4, 5, 6, 7])

fuel_type = st.selectbox("Fuel Type", ["Petrol", "Diesel", "CNG"])
seller_type = st.selectbox("Seller Type", ["Individual", "Dealer"])
transmission = st.selectbox("Transmission Type", ["Manual", "Automatic"])

# Prepare input data
input_data = pd.DataFrame({
    "vehicle_age": [vehicle_age],
    "km_driven": [km_driven],
    "mileage": [mileage],
    "engine": [engine],
    "max_power": [max_power],
    "seats": [seats],
    "fuel_type_Diesel": [1 if fuel_type == "Diesel" else 0],
    "fuel_type_Petrol": [1 if fuel_type == "Petrol" else 0],
    "seller_type_Individual": [1 if seller_type == "Individual" else 0],
    "transmission_type_Manual": [1 if transmission == "Manual" else 0]
    
})

# Add missing columns
for col in columns:
    if col not in input_data.columns:
        input_data[col] = 0

# Arrange columns
input_data = input_data[columns]

# Prediction
if st.button("Predict Price"):
    prediction = model.predict(input_data)
    st.success(f"💰 Predicted Car Price: ₹ {int(prediction[0]):,}")



