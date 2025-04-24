import requests
import os
from twilio.rest import Client
from dotenv import load_dotenv

load_dotenv()

URL = "https://api.openweathermap.org/data/2.5/forecast"

api_key = os.getenv("api_key")

acc_sid = os.getenv("acc_sid")
autoke = os.getenv("autoke")


client = Client(acc_sid, autoke)


PARAMETERS = {
    "lat": os.getenv("latitude"),
    "lon": os.getenv("longitude"),
    "appid": api_key,
    "cnt": 4
}

response = requests.get(URL, params=PARAMETERS)
response.raise_for_status()
print(response.status_code)
data = response.json()
# print(data)
will_rain = False


for hour_data in data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if condition_code < 700:
        will_rain = True

if will_rain:
    message = client.messages.create(
        from_=f"whatsapp:{os.getenv("F_Number")}",
        body="The Weather bad today bring your umbrella if you go out",
        to=f"whatsapp:{os.getenv("T_Number")}"
    )

    # print(message.status)