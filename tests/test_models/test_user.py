#!/usr/bin/python3
"""User Unittest Module
"""

from models.user import User
import unittest
from datetime import datetime
import pycodestyle


class TestUser(unittest.TestCase):
    """
    User TestCases
    """

    def test_basemodel_id(self):
        """ test if the User is a string"""
        model = User()
        self.assertIsInstance(model.id, str)

    def test_updated_at_format(self):
        """ test if updated at is a datetime"""
        model = User()
        self.assertIsInstance(model.updated_at, datetime)

    def test_created_at_format(self):
        """ test if created at is a datetime"""
        model = User()
        self.assertIsInstance(model.created_at, datetime)

    def test_create_from_dict(self):
        """test create model from dictionary
        """
        kwargs = {'my_number': 89,
                  'name': 'My First Model',
                  '__class__': 'User',
                  'updated_at': '2017-09-28T21:05:54.119572',
                  'id': 'b6a6e15c-c67d-4312-9a75-9d084935e579',
                  'created_at': '2017-09-28T21:05:54.119427'}
        model = User(**kwargs)
        self.assertEqual(model.__class__.__name__, 'User')
        self.assertEqual(model.id, 'b6a6e15c-c67d-4312-9a75-9d084935e579')
        self.assertEqual(model.my_number, 89)

    def test_conformance(self):
        """Test that we conform to PEP-8."""
        style = pycodestyle.StyleGuide(quiet=True)
        result = style.check_files(['models/user.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")
