import json
import requests

city = input("Enter the name of the city\n")

url = f"http://api.weatherapi.com/v1/current.json?key=ff74faeef856471fbed123052231908&q={city}"

r = requests.get(url)
wdic = json.loads(r.text)
w = (wdic["current"]["temp_c"])
print("Temperature: " , w , "%c")
