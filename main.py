import streamlit as st
import plotly.express as px

st.title("Weather forecast for upcoming days")
place = st.text_input("Place: ")
days = st.slider("Forecast Days", min_value=1, max_value=5)
option = st.selectbox("Select the data to view", ("Temperature", "Sky"))
st.subheader(f"{option} for the next {days} days in {place}")

def get_data(days):
    dates = ["2024-01-16", "2024-01-17", "2024-01-18"]
    temperatures = [10, 11, 12]
    temperatures = [days * i for i in temperatures]
    return dates, temperatures


d, t = get_data(days)

figure = px.line(x=d, y=t, labels={"x": "Date", "y": "Temperature (C)"})
st.plotly_chart(figure)
