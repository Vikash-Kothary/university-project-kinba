#! python3
# weather.py -

# Makes it compatible with Python 2.7 and 3.x
from __future__ import print_function
from settings import OPENWEATHERMAP_KEY
from pyowm import OWM


if __name__ == '__main__':
    owm = pyowm.OWM(OPENWEATHERMAP_KEY)
    observation = owm.weather_at_place("London, uk")
    w = observation.get_weather()
    print(w.get_temperature('celsius'))
