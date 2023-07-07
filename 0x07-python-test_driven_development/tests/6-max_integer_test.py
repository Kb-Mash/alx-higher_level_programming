#!/usr/bin/python3
# 6-max_integer_test.py
"""Unittests for max_integer([..])."""

import unittest
max_integer = __import__('6-max_integer').max_integer

class MaxIntegerTestCase(unittest.TestCase):
    """Define unittests for max_integer([..])."""
    def test_empty_list(self):
        """Test with an empty list"""
        result = max_integer([])
        self.assertIsNone(result)

    def test_positive_integers(self):
        """Test with a list of positive integers"""
        result = max_integer([1, 3, 5, 2, 4])
        self.assertEqual(result, 5)

    def test_negative_integers(self):
        """Test with a list of negative integers"""
        result = max_integer([-1, -3, -5, -2, -4])
        self.assertEqual(result, -1)

    def test_mixed_integers(self):
        """Test with a list of mixed positive and negative integers"""
        result = max_integer([1, -3, 5, -2, 4])
        self.assertEqual(result, 5)

    def test_single_element(self):
        """Test with a list containing a single element"""
        result = max_integer([7])
        self.assertEqual(result, 7)

    def test_duplicate_values(self):
        """Test with a list containing duplicate values"""
        result = max_integer([3, 2, 3, 1, 1])
        self.assertEqual(result, 3)

if __name__ == "__main__":
    unittest.main()

