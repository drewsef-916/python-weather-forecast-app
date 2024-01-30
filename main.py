import streamlit as st

st.title("Weather forecast for upcoming days")
place = st.text_input("Place: ")
days = st.slider("Forecast Days", min_value=1, max_value=5)
option = st.selectbox("Select the data to view", ("Temperature", "Sky"))
st.subheader(f"{option} for the next {days} days in {place}")