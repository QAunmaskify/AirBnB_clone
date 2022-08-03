#!/usr/bin/python3
"""
Test file for the BaseModel class
"""
from models.base_model import BaseModel
from datetime import datetime
import unittest

class TestBaseModel(unittest.TestCase):
    """ Unit testing cases"""
    def test_init(self):
        my_model_json = {'id': '097351d0-1062-404b-92f4-06ee12d19b3f',
                    'created_at': '2022-08-02T21:01:51.415101',
                    'updated_at': '2022-08-02T21:01:51.415118',
                    'name': 'My_First_Model', 'my_number': 89,
                    '__class__': 'BaseModel'}
        my_model = BaseModel(**my_model_json)
        self.assertEqual(type(my_model.created_at), datetime)

    def test_save(self):
        pass
