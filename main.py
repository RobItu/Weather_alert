import os
import requests
from twilio.rest import Client

API_KEY = "cc3f2019713b5a7a28e8e68f77e9e955"
LAT = 30.49
LON = -83.278

weather_parameters = {
    "lat": LAT,
    "lon": LON,
    "appid": API_KEY,
    "exclude": "current,minutely,daily"
}

OWM_API = "https://api.openweathermap.org/data/2.5/onecall"
response = requests.get(url=OWM_API, params=weather_parameters)

weather_data = response.json()
weather_hourly = weather_data["hourly"]
weather_id_list = []

will_rain = False
for section in range(12):
    id = weather_hourly[section]["weather"][0]["id"]
    if id < 700:
        will_rain = True

if will_rain:
    client = Client(os.environ["account_sid"], os.environ['auth_token'])
    message = client.messages \
        .create(
        body="It's going to rain today, you'll need an umbrella ☂️",
        from_='+12073869879',
        to='+1##########'
    )
    print(message.status)
