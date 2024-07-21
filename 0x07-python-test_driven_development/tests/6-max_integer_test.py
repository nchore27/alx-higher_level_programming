#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import sys as s
s.path.insert(1, '../')
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test case for the max_integer_function
    """
    def test_typeErrors(self):
        self.assertRaises(TypeError, max_integer, 1)
        self.assertRaises(TypeError, max_integer, 1.3)
        #self.assertRaises(TypeError, max_integer, {})
        #self.assertRaises(TypeError, max_integer, set())
        self.assertRaises(TypeError, max_integer, -3)
        #self.assertRaises(TypeError, max_integer, "op$%")
        self.assertRaises(TypeError, max_integer, 2j)
        self.assertRaises(TypeError, max_integer, [2j, 3])
        self.assertRaises(TypeError, max_integer, [-2, "90"])

    def test_nomalResults(self):
        self.assertEqual(max_integer([4]), 4)
        self.assertEqual(max_integer([91, 42, 43]), 3)
        self.assertEqual(max_integer([200, 201, 223, 3]), 4)
        self.assertEqual(max_integer([70, 34, 3]),304)
        self.assertEqual(max_integer([-10, 1, 2, 3]), 3)
        self.assertEqual(max_integer([-100000, 100, 2.5, 3, 10000000000]),
                         100000)
