import matplotlib.pyplot as plt
import streamlit as st

def plot_temperature_trends(days, max_temps, min_temps):
    """
    Plot temperature trends for 7 days.
    """
    plt.figure(figsize=(10, 5))
    plt.plot(days, max_temps, label="Max Temp (°C)", marker='o', linestyle='-', color='red')
    plt.plot(days, min_temps, label="Min Temp (°C)", marker='o', linestyle='-', color='blue')
    plt.title("7-Day Temperature Trend")
    plt.xlabel("Days")
    plt.ylabel("Temperature (°C)")
    plt.legend()
    plt.grid(True)
    st.pyplot(plt)

def plot_precipitation(days, precipitations):
    """
    Plot daily precipitation as a bar chart.
    """
    plt.figure(figsize=(10, 5))
    plt.bar(days, precipitations, color='blue')
    plt.title("Daily Precipitation (mm)")
    plt.xlabel("Days")
    plt.ylabel("Precipitation (mm)")
    st.pyplot(plt)

def plot_wind_speed(days, wind_speeds):
    """
    Plot wind speed trends.
    """
    plt.figure(figsize=(10, 5))
    plt.plot(days, wind_speeds, label="Wind Speed (m/s)", marker='o', linestyle='-', color='green')
    plt.title("7-Day Wind Speed Trend")
    plt.xlabel("Days")
    plt.ylabel("Wind Speed (m/s)")
    plt.legend()
    plt.grid(True)
    st.pyplot(plt)
