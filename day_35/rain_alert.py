import requests
from twilio.rest import Client

api_key = "6bcc9bf4d73d63b48ded1ffdf27c1c41"

account_sid = "ACe47824692a784dc0c668b27ad3478f8e"
auth_token = "3a3672d25b561384fc3654f5e5302c7a"

parameters = {
    "lat": 52.2298,
    "lon": 21.0118,
    "appid": api_key,
    "exclude": "current,minutely,daily"
}

response = requests.get(url="https://api.openweathermap.org/data/2.5/onecall", params=parameters)
response.raise_for_status()
weather_data = response.json()
weather_data_hours = weather_data["hourly"]

if_rain = True
if_snow = False

for hour in weather_data_hours[:12]:
    code = hour["weather"][0]["id"]
    if 700 > code >= 600:
        if_snow = True
    elif 600 > code >= 200:
        if_rain = True

if if_rain or if_snow:
    client = Client(account_sid, auth_token)
    if if_rain:
        message = client.messages.create(
            body="Bedzie dzisiaj padal deszcz",
            from_="+18647347031",
            to="receiver phone number")
    else:
        message = client.messages.create(
            body="Bedzie dzisiaj padal snieg",
            from_="+18647347031",
            to="receiver phone number")
    print(message.status)
