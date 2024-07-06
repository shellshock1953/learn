import unittest
from city_functions import city_country 

class CityCountryTest(unittest.TestCase):

    def test_city_country(self):
        formated_city = city_country('Lviv', 'Ukraine')
        self.assertEqual(formated_city, 'Lviv, Ukraine')

    def test_population(self):
        formated_population = city_country('Odessa', 'Ukraine', 993_000)
        self.assertEqual(formated_population, 'Odessa, Ukraine - population 993000')

if __name__ == "__main__":
    unittest.main()
