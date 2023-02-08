import requests
import pprint
api_key = "339356088c77e54e90b6f292f16f06f7"
City_name = input("Enter city name: ")
country_code = "IN"
base_url = "https://api.openweathermap.org/data/2.5/weather?"
complete_url = base_url + "appid=" + api_key + "&q=" + City_name + "," + country_code
response = requests.get(complete_url)
weather_data = response.json()
pprint.pprint(weather_data)



