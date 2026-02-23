import streamlit as st
import requests


# -------- Weather Function --------
def get_weather(lat, lon):

    url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"

    response = requests.get(url)
    data = response.json()

    temperature = data["current_weather"]["temperature"]
    windspeed = data["current_weather"]["windspeed"]

    return temperature, windspeed

# -------- Streamlit UI --------
st.title("EcoRoute AI")
st.write("Smart Tourism Planning & Carbon-Aware Travel")

if st.button("Generate Smart Itinerary"):

    lat = 13.0827
    lon = 80.2707

    temp, wind = get_weather(lat, lon)

    st.write("Current Temperature:", temp, "°C")
    st.write("Wind Speed:", wind, "km/h")