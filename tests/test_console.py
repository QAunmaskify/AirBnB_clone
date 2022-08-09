#!/usr/bin/python3
"""HBNBCommand Unittest Module
"""

import console
import unittest
import pycodestyle


class TestHBNBCommand(unittest.TestCase):
    """
    HBNBCommand TestCases
    """

    def test_conformance_console(self):
        """Test that console.py conform to PEP-8."""
        style = pycodestyle.StyleGuide(quiet=True)
        result = style.check_files(['console.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_conformance_test_console(self):
        """Test that tests/test_console.py conform to PEP-8."""
        style = pycodestyle.StyleGuide(quiet=True)
        result = style.check_files(['tests/test_console.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")
