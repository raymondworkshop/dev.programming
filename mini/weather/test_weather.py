import os
import pytest

import weather

def test_get_api_key():
    assert weather.get_api_key() == "03a706387cfd23c1d9ff44e3d1e03f97"

def test_build_weather_query():
    city_name = ['hong', 'kong']
    print(weather.build_weather_query(city_name))
