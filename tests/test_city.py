#!/usr/bin/python3
""" Test City File """
import unittest
from models.city import City


class Test_City(unittest.TestCase):
    """ Test State Class """

    def test_name_string(self):
        """ Test not a single character """
        self.assertEqual(type(City().name), str)
        """ Test id """
