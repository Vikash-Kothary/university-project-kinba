#!/usr/bin/env python3
# weather.py -

from pyowm import OWM
from pyowm.caches.lrucache import LRUCache

BAD_WEATHER = 'cloudy'
GOOD_WEATHER = 'sunny'

def main():
    API_KEY = '7c256dfe06b95f67bc5cf3686cef1c5a'
    owm = OWM(API_KEY)
    #cache = LRUCache()
    
	# Longitude and latitude for Strand campus
    forecast = owm.weather_at_coords(51.5114897, -0.118191).get_weather()
    temperature = forecast.get_temperature(unit='celsius')['temp']
    status = good_or_bad_weather(forecast.get_status(), forecast.get_weather_code())
    response = to_speech(predicted=GOOD_WEATHER, actual=status, temperature=temperature)
    print(response)

def good_or_bad_weather(weather_condition, weather_code):
	if str(weather_code)[:2] == '80':
		return GOOD_WEATHER
	if str(weather_code)[:2] == '95' and int(str(weather_code)[-1]) < 5:
		return GOOD_WEATHER 
	return BAD_WEATHER

def to_speech(predicted, actual, temperature):
	success = 'wrong'
	if predicted == actual:
		success = 'right'
	return 'I was %s it is %s outside. Temperature is %s degrees celsius' % (success, actual, temperature)

if __name__ == '__main__':
    main()
