#!/usr/bin/python3
"""State Unittest Module
"""

from models.state import State
import unittest
from datetime import datetime
import pycodestyle


class TestState(unittest.TestCase):
    """
    State TestCases
    """

    def test_basemodel_id(self):
        """ test if the State is a string"""
        model = State()
        self.assertIsInstance(model.id, str)

    def test_updated_at_format(self):
        """ test if updated at is a datetime"""
        model = State()
        self.assertIsInstance(model.updated_at, datetime)

    def test_created_at_format(self):
        """ test if created at is a datetime"""
        model = State()
        self.assertIsInstance(model.created_at, datetime)

    def test_create_from_dict(self):
        """test create model from dictionary
        """
        kwargs = {'city': 'Lagos',
                  '__class__': 'State',
                  'updated_at': '2017-09-28T21:05:54.119572',
                  'id': 'b6a6e15c-c67d-4312-9a75-9d084935e579',
                  'created_at': '2017-09-28T21:05:54.119427'}
        model = State(**kwargs)
        self.assertEqual(model.__class__.__name__, 'State')
        self.assertEqual(model.id, 'b6a6e15c-c67d-4312-9a75-9d084935e579')

    def test_conformance(self):
        """Test that we conform to PEP-8."""
        style = pycodestyle.StyleGuide(quiet=True)
        result = style.check_files(['models/state.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_conformance_state(self):
        """Test that we conform to PEP-8."""
        style = pycodestyle.StyleGuide(quiet=True)
        result = style.check_files(['tests/test_models/test_state.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")
