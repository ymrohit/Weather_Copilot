import requests
import sys
import json
import datetime
import pycountry

#write a function that maps country codes to country names using pycountry
def get_country_name(country_code):
    country_name = pycountry.countries.get(alpha_2=country_code)
    return country_name.name


#write a function that takes a city name and returns the weather
def get_weather(city_name):
    #get the weather
    url = "http://api.openweathermap.org/data/2.5/weather?q=" + city_name + "&appid=f5a4b89921176ef3d314a60e487fdbc8"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

#write a function that takes a weather dictionary and prints the weather
def print_weather(weather):
    if weather != None:
        print("The weather in " + weather["name"] + " is " + weather["weather"][0]["description"])
    else:
        print("Error: Could not get weather")

#write a function that takes a weather dictionary and prints the temperature in degrees celsius with degree symbol while rounding to 2 decimal places
def print_temp_celsius(weather):
    if weather != None:
        print("The temperature in " + weather["name"] + " is " + str(round(weather["main"]["temp"] - 273.15,1)) + "°C")
    else:
        print("Error: Could not get temperature")

#write a function that takes a weather dictionary and prints the temperature in degrees fahrenheit with degree symbol while rounding to 2 decimal places
def print_temp_fahrenheit(weather):
    if weather != None:
        print("The temperature in " + weather["name"] + " is " + str(round(((weather["main"]["temp"] - 273.15) * 9/5 + 32),1)) + "°F")
    else:
        print("Error: Could not get temperature")

#write a function that takes a weather dictionary and prints the humidity with units
def print_humidity(weather):
    if weather != None:
        print("The humidity in " + weather["name"] + " is " + str(weather["main"]["humidity"]) + "%")
    else:
        print("Error: Could not get humidity")


#write a function that takes a weather dictionary and prints the wind speed with units
def print_wind(weather):
    if weather != None:
        print("The wind speed in " + weather["name"] + " is " + str(weather["wind"]["speed"]) + "m/s")
    else:
        print("Error: Could not get wind speed")

#write a function that takes a weather dictionary and prints the pressure with units
def print_pressure(weather):
    if weather != None:
        print("The pressure in " + weather["name"] + " is " + str(weather["main"]["pressure"]) + "hPa")
    else:
        print("Error: Could not get pressure")
        
#write a function that takes a weather dictionary and prints the latitude and longitude with units
def print_lat_lon(weather):
    if weather != None:
        print("The latitude and longitude in " + weather["name"] + " is " + str(weather["coord"]["lat"]) + ", " + str(weather["coord"]["lon"]))
    else:
        print("Error: Could not get latitude and longitude")

#write a function that takes a weather dictionary and prints the sunrise and sunset and show correct time in local time
def print_sun(weather):
    if weather != None:
        sunrise = datetime.datetime.fromtimestamp(weather["sys"]["sunrise"])
        sunset = datetime.datetime.fromtimestamp(weather["sys"]["sunset"])
        print("The sunrise and sunset in " + weather["name"] + " is " + str(sunrise) + ", " + str(sunset))
    else:
        print("Error: Could not get sunrise and sunset")



#write a function that takes a weather dictionary and prints the full country name
def print_country(weather):
    if weather != None:
        country_name = get_country_name(weather["sys"]["country"])
        print("The country name in " + weather["name"] + " is " + country_name)
    else:
        print("Error: Could not get country name")

#write a function that takes city name in command line arguments and prints complete weather information
def main():
    if len(sys.argv) != 2:
        print("Error: Please enter a city name")
    else:
        city_name = sys.argv[1]
        weather = get_weather(city_name)
        print_weather(weather)
        print_temp_celsius(weather)
        print_temp_fahrenheit(weather)
        print_humidity(weather)
        print_wind(weather)
        print_pressure(weather)
        print_lat_lon(weather)
        print_sun(weather)
        print_country(weather)

if __name__ == "__main__":
    main()
    
