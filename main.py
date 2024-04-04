import requests
from twilio.rest import Client

account_sid = "ACdbe586da7d3e41c2da294a9a22d49e66"
auth_token = "b24b39672d771a4fb1747311ccf1f1f8"



MY_KEY = "ad9f69824d7efd12d311f291256f065c"
MY_LINK = "https://api.openweathermap.org/data/2.5/forecast"

parameters = {
    "lat": 17.385044,
    "lon":78.486671 ,
    "appid": MY_KEY,
     "cnt": 4
}

response = requests.get(MY_LINK, params=parameters)
response.raise_for_status()
data= response.json()
rain= False
for hourdata in data["list"]:
    condition = hourdata["weather"][0]["id"]
    if int(condition)<700:
        rain=True

if rain:
   client=Client(account_sid,auth_token)
   massage= client.messages\
            .create(
       body="it is going to rain today. remember to bring umbralla",
       from_="+13346058007",
       to="+9178931 36201 ")
   print(massage.Status)




