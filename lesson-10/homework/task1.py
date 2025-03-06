import requests


MY_LAT = 41.255178
MY_LONG = 69.436596
MY_ID = "fe7e1e7023a076928e95dc50dc7ce427"

parameters = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": MY_ID
}

url = "https://api.openweathermap.org/data/2.5/weather"
response = requests.get(url=url, params=parameters)

data = response.json()

temp = data["main"]["temp"] - 273.15
temp = round(temp, 2)

feel_temp = data["main"]["feels_like"] - 273.15
feel_temp = round(feel_temp, 2)

humidity = data["main"]["humidity"]

wind_speed = data["wind"]["speed"] * 1.6

print("Weather details in Tashkent for 6th march: ")

print("Temperature: ", end="")
print(temp, end=" ")
print(f"(Feels like {feel_temp})")
print("humidity:", + humidity)
print("Wind speed:", + wind_speed)
