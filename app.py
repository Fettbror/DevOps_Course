import streamlit as st
from get_weather_data import fetch_weather_data
from dashboard import plot_temperature_trends, plot_precipitation, plot_wind_speed

# Cities and their coordinates
city_coordinates = {
    "Stockholm": (59.334591, 18.063240),
    "Göteborg": (57.708870, 11.974560),
    "Malmö": (55.605870, 13.000730)
}

st.title("Weather App for Selected Cities")

selected_city = st.selectbox("Choose a city", list(city_coordinates.keys()))

if st.button("Get Weather"):
    try:

        lat, lon = city_coordinates[selected_city]
        st.write(f"Fetching weather data for {selected_city}...")


        data = fetch_weather_data(lat, lon)

        if 'daily' in data:
            st.subheader(f"7-Day Weather Overview for {selected_city}")


            days = [f"Day {i+1}" for i in range(len(data['daily']))]
            max_temps = [day['temp']['max'] for day in data['daily']]
            min_temps = [day['temp']['min'] for day in data['daily']]
            precipitations = [day.get('rain', 0) for day in data['daily']]
            wind_speeds = [day['wind_speed'] for day in data['daily']]


            plot_temperature_trends(days, max_temps, min_temps)
            plot_precipitation(days, precipitations)
            plot_wind_speed(days, wind_speeds)

        else:
            st.write("No data available for this location.")

    except Exception as e:
        st.error(e)
