import requests
import datetime

MY_LAT = 51.507351
MY_LONG = -0.747553

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise_hour = data["results"]["sunrise"].split('T')[1].split(":")[0]
sunset_hour = data["results"]["sunset"].split('T')[1].split(":")[0]

date = datetime.datetime.now().hour
