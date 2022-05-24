#!/usr/bin/python3
"""
unitest
"""

import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_int_list(self):
        self.assertEqual(max_integer([2, 5, 6]), 6)
        self.assertEqual(max_integer([6, 5, 2]), 6)
        self.assertEqual(max_integer([2, 6, 5]), 6)

    def test_empty_list(self):
        self.assertEqual(max_integer([]), None)

    def test_float_list(self):
        self.assertEqual(max_integer([1.1, 2.2, 3.3]), 3.3)

    def test_string_list(self):
        self.assertEqual(max_integer(["Jack Sparrow"]), "Jack Sparrow")


