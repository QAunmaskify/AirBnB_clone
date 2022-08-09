#!/usr/bin/python3
"""City Unittest Module
"""

from models.city import City
import unittest
from datetime import datetime
import pycodestyle


class TestCity(unittest.TestCase):
    """
    City TestCases
    """

    def test_basemodel_id(self):
        """ test if the City is a string"""
        model = City()
        self.assertIsInstance(model.id, str)

    def test_updated_at_format(self):
        """ test if updated at is a datetime"""
        model = City()
        self.assertIsInstance(model.updated_at, datetime)

    def test_created_at_format(self):
        """ test if created at is a datetime"""
        model = City()
        self.assertIsInstance(model.created_at, datetime)

    def test_create_from_dict(self):
        """test create model from dictionary
        """
        kwargs = {'my_number': 89,
                  'name': 'My First Model',
                  '__class__': 'City',
                  'updated_at': '2017-09-28T21:05:54.119572',
                  'id': 'b6a6e15c-c67d-4312-9a75-9d084935e579',
                  'created_at': '2017-09-28T21:05:54.119427'}
        model = City(**kwargs)
        self.assertEqual(model.__class__.__name__, 'City')
        self.assertEqual(model.id, 'b6a6e15c-c67d-4312-9a75-9d084935e579')
        self.assertEqual(model.my_number, 89)

    def test_conformance(self):
        """Test that we conform to PEP-8."""
        style = pycodestyle.StyleGuide(quiet=True)
        result = style.check_files(['models/city.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_conformance_city(self):
        """Test that we conform to PEP-8."""
        style = pycodestyle.StyleGuide(quiet=True)
        result = style.check_files(['tests/test_models/test_city.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")
