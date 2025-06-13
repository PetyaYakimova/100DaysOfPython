import requests

OWM_ENDPOINT = "https://api.openweathermap.org/data/2.5/forecast"
API_KEY = "key"

params = {
    "lat": 42.6332215,
    "lon": 23.3772876,
    "appid": API_KEY,
    "cnt": 4,
}

response = requests.get(OWM_ENDPOINT, params=params)
response.raise_for_status()
weather_data = response.json()

will_rain = False
for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    print("Bring an umbrella")
