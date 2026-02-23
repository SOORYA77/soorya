import streamlit as st

def calculate_carbon(distance_km, mode):

    emission_factors = {
        "car": 0.21,
        "bus": 0.10,
        "bike": 0.05,
        "walk": 0
    }

    return distance_km * emission_factors[mode]


st.title("Carbon Calculation Demo")

if st.button("Calculate Carbon"):

    travel_time_minutes = 20
    average_speed = 30  # km/h
    mode = "car"

    distance_km = (travel_time_minutes / 60) * average_speed

    carbon = calculate_carbon(distance_km, mode)

    st.write("Distance:", round(distance_km, 2), "km")
    st.write("Estimated Carbon Emission:", round(carbon, 2), "kg CO2")