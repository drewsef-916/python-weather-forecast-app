import requests

API_KEY = "68ba548b9863e2c8ae3bfe44e1ea73a4"

def get_data(place, forecast_days):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()
    filtered_data = data["list"]
    num_values = 8 * forecast_days
    filtered_data = filtered_data[:num_values]
    return filtered_data
