#!/usr/bin/env python3
# weather.py -

from pyowm import OWM
from pyowm.caches.lrucache import LRUCache


def main():
    API_KEY = '7c256dfe06b95f67bc5cf3686cef1c5a'
    owm = OWM(API_KEY)
    cache = LRUCache()


def get_forcast(owm):
    forecast = owm.weather_at_place(51.5114897, -0.118191).get_weather()
    forcast.get_clouds()
    forcast.get_rain()
    forcast.get_temperature()
    forcast.get_status()


if __name__ == '__main__':
    main()
