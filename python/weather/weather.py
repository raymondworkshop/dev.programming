# weather.py

import configparser
import argparse

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
    """
    """
    return

def main():
    print(get_api_key())
    args = read_cli_args()
    print(args.city, args.imperial)
    #
    build_weather_query(args.city, args.imperial)


if __name__ == "__main__":
    main()