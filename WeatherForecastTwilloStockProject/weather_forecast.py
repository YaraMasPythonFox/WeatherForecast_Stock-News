import requests
from twilio.rest import Client

LONGITUDE = '**30.542721'
LATITUDE = '**50.447731'
API_KEY = "api"
CNT = 4
account_sid = "account_sid"
auth_token = "auth_token "
trial_phone = "Your twillo trial_phone"


weather_params= {"lon": LONGITUDE,
        "lat": LATITUDE,
        "appid":API_KEY,
           "cnt": CNT,
}
response = requests.get(url='https://api.openweathermap.org/data/2.5/forecast', params=weather_params)
response.raise_for_status()
weather_data=response.json()

will_rain = False
for hour_data in weather_data["list"]:
    condition_code=hour_data["weather"][0]['id']
    if condition_code < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body="Bring an umbrella!. Today will be rainy!",
        from_= trial_phone,
        to="Your phone",
    )
    print(message.status)
else:
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body="Don't bring an umbrella!. Today will be sunny!",
        from_=trial_phone,
        to="Your phone",
    )

    print(message.status)