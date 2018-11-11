# -*- coding: utf-8 -*-
"""
Created on Wed Aug  1 16:34:16 2018

@author: Editi
"""

import  unittest
from city_function import city_describe


class CityCountryTestCase(unittest.TestCase):
    def test_city_country(self):
        city_country_info = city_describe('beijing','china','2400')
        self.assertEqual(city_country_info,'Beijing , China , Poplutation: 2400')
        

unittest.main()