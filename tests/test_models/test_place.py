#!/usr/bin/python3
"""Place Unittest Module
"""

from models.place import Place
import unittest
from datetime import datetime
import pycodestyle


class TestPlace(unittest.TestCase):
    """
    Place TestCases
    """

    def test_basemodel_id(self):
        """ test if the Place is a string"""
        model = Place()
        self.assertIsInstance(model.id, str)

    def test_updated_at_format(self):
        """ test if updated at is a datetime"""
        model = Place()
        self.assertIsInstance(model.updated_at, datetime)

    def test_created_at_format(self):
        """ test if created at is a datetime"""
        model = Place()
        self.assertIsInstance(model.created_at, datetime)

    def test_create_from_dict(self):
        """test create model from dictionary
        """
        kwargs = {'place_id': 89,
                  'place': 'Lekki',
                  '__class__': 'Place',
                  'updated_at': '2017-09-28T21:05:54.119572',
                  'id': 'b6a6e15c-c67d-4312-9a75-9d084935e579',
                  'created_at': '2017-09-28T21:05:54.119427'}
        model = Place(**kwargs)
        self.assertEqual(model.__class__.__name__, 'Place')
        self.assertEqual(model.id, 'b6a6e15c-c67d-4312-9a75-9d084935e579')
        self.assertEqual(model.place_id, 89)

    def test_conformance(self):
        """Test that we conform to PEP-8."""
        style = pycodestyle.StyleGuide(quiet=True)
        result = style.check_files(['models/place.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_conformance_place(self):
        """Test that we conform to PEP-8."""
        style = pycodestyle.StyleGuide(quiet=True)
        result = style.check_files(['tests/test_models/test_place.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")
