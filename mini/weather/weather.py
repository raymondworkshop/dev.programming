# weather.py

import configparser
import argparse
#from urllib import parse
import requests
import json
import sys
from pprint import pp

BASE_WEATHER_API_URL = "http://api.openweathermap.org/data/2.5/weather"


def get_api_key():
    """Fetch the API key from configuration file"""
    config = configparser.ConfigParser()
    config.read('/Users/zhaowenlong/workspace/proj/dev.programming/python/weather/secrets.ini')

    return config["openweather"]["api_key"]

def read_cli_args():
    """handles CLI interactions

        returns:

    """
    parser = argparse.ArgumentParser(
        description="get weather and temperature information for a city"
    )
    parser.add_argument("city", nargs="+", type=str, help="enter the city name")
    parser.add_argument(
    "-i", 
    "--imperial",
    action="store_true",
    help="display the temperature in imperial units")
    
    return parser.parse_args()


def build_weather_query(city, imperial=False):
    """ Build the URL for an API request to OpenWeather's weather API
        
        args:
            city: (list[str])
            imperial (bool)
        returns:
            str: URL 
    """
    api_key = get_api_key()
    city_name = " ".join(city)
    url_encoded_city_name = parse.quote_plus(city_name)
    units = "imperial" if imperial else "metric"
    url = (
        f"{BASE_WEATHER_API_URL}?q={url_encoded_city_name}"
        f"&units={units}&appid={api_key}"
    )
    return url

def get_weather_data(city, imperial=False):
    """Build the URL for an API request to OpenWeather's weather API
        
        args:
            city: (list[str])
            imperial (bool)
        returns:
            dict: Weather information for a specific city
    """
    api_key = get_api_key()
    city_name = " ".join(city)
    #url_encoded_city_name = parse.quote_plus(city_name)
    url_encoded_city_name = requests.utils.quote(city_name)
    units = "imperial" if imperial else "metric"
    params = {
        "q" : city_name,
        "units" : units,
        "appid" : api_key
    }

    r = requests.get(BASE_WEATHER_API_URL, params=params)
    print(r.url)
    if r.status_code == requests.codes.ok: #OK
        weather_data = r.json()
    elif r.status_code == 404: # Not Found
        sys.exit("Can't find weather data for this city")
    else:
        pass

    return weather_data


def display_weather_info(weather_data, imperial=False):
    """Prints formatted weather information about a city.

    Args:
       weather_data (dict):
       imperial (bool):
        
    """
    city = weather_data["name"]
    weather_description = weather_data["weather"][0]["description"]
    temperature = weather_data["main"]["temp"]

    weather = (
        f"{city:^20}"
        f"\t{weather_description.capitalize():^20} "
        f"({temperature}°{'F' if imperial else 'C'})"
    )
    print(weather)


def main():
    #print(get_api_key())
    args = read_cli_args()
    print(args.city, args.imperial)
    #
    weather_data = get_weather_data(args.city, args.imperial)
    #pp(weather_data)
    display_weather_info(weather_data, args.imperial)


if __name__ == "__main__":
    main()