import requests
import os
from twilio.rest import Client

# open weather api Key
api_key = os.environ.get("OWM_API_KEY")

# twilio account sid and auth token
account_sid = os.environ.get("AUTH_ID")
auth_token = os.environ.get("AUTH_TOKEN")

client = Client(account_sid, auth_token)

MY_LAT= 24.8970
MY_LON= 67.2136

parameter = {
    "lat": MY_LAT,
    "lon":MY_LON,
    "cnt":4,
    "appid": api_key
}

response = requests.get(url = "https://api.openweathermap.org/data/2.5/forecast", params=parameter)
response.raise_for_status()

weather_data = response.json()

weather_id = [weather_data['list'][i]['weather'][0]['id'] for i in range(int(weather_data['cnt']))]

if any(w_id < 600 for w_id in weather_id):

    message = client.messages.create(
        from_='whatsapp:---TRIAL NUMBER---',
        body= "It's going to rain today, Don't forget to bring an Umbrella ☔",
        to='whatsapp:---VERIFIED NUMBER---'
    )
    print(message.status)
else:
    message = client.messages.create(
        from_='whatsapp:---TRIAL NUMBER---',
        body="No chances of rain, You are good to go 😊",
        to='whatsapp:---VERIFIED NUMBER---'
    )

