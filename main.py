import requests, json
from pprint import pprint
API_KEY='dafd97f003d8a26e3f8751477078ef34'
city=input("Enter City Name")
baseurl="https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid="+API_KEY
data=requests.get(baseurl).json()
print(data)

