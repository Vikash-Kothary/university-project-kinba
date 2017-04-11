#! python3
# test_weather.py -

# Makes it compatible with Python 2.7 and 3.x
from __future__ import print_function
from settings import OPENWEATHERMAP_KEY
from pyowm import OWM
import unittest


class TestWeather(unittest.TestCase):

    def setUp(self):
        self.owm = OWM(OPENWEATHERMAP_KEY)

    def testCorrectAPIKey(self):
        expected = OPENWEATHERMAP_KEY
        actual = owm.get_API_key()
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
    owm = OWM(OPENWEATHERMAP_KEY)
    observation = owm.weather_at_place("London, uk")
    w = observation.get_weather()
    print(w.get_temperature('celsius'))
