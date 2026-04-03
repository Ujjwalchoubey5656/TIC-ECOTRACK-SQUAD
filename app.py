## frontend
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
import os

# ---------------- CONFIG ----------------
st.set_page_config(page_title="EcoTrack AI", page_icon="🌱")

st.title("🌱 EcoTrack AI")
st.markdown("### Smart Carbon Footprint Tracker")

# ---------------- SIDEBAR ----------------
st.sidebar.header("Enter Your Details")

distance = st.sidebar.number_input("🚗 Distance (km)", min_value=0.0, value=5.0)

transport = st.sidebar.selectbox(
    "Transport",
    ["Car", "Bike", "Bus", "Train"]
)

electricity = st.sidebar.number_input("⚡ Electricity Units", min_value=0.0, value=3.0)

food = st.sidebar.selectbox("🍽️ Food Type", ["Veg", "Non-Veg"])








## Bckened
factors = {
    "Car": 0.2,
    "Bike": 0.1,
    "Bus": 0.05,
    "Train": 0.04
}

ELECTRICITY_CO2 = 0.82


#--------------data storage___________#
data = {
    "Date": datetime.now().strftime("%Y-%m-%d %H:%M"),
    "Transport": transport,
    "Distance": distance,
    "Electricity": electricity,
    "Food": food,
    "CO2": total
}

df = pd.DataFrame([data])

file = "data.csv"

if os.path.exists(file):
    df.to_csv(file, mode='a', header=False, index=False)
else:
    df.to_csv(file, index=False)


#----------------------data fetch backend__________#
if os.path.exists(file):
    history = pd.read_csv(file)


#___________________analytics backend_______#
weekly_avg = history["CO2"].tail(7).mean()
monthly_avg = history["CO2"].tail(30).mean()

transport_group = history.groupby("Transport")["CO2"].mean()





   












## Database

















##ai intergeration
transport_co2 = distance * factors[transport]
electricity_co2 = electricity * ELECTRICITY_CO2
food_co2 = 2 if food == "Veg" else 5

total = transport_co2 + electricity_co2 + food_co2
#looping
if total > 10:
    st.warning("Reduce emissions! Use public transport & save electricity.")
else:
    st.success("Great job! You're eco-friendly!")

if food == "Non-Veg":
    st.write("Try plant-based meals 2–3 times a week")

if electricity > 5:
    st.write("Turn off unused appliances")
