#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Test cases for the max_integer function"""

    def test_regular_case(self):
        """Test case for a normal list of integers"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_negative_numbers(self):
        """Test case for a list with negative numbers"""
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_single_element(self):
        """Test case for a list with only one element"""
        self.assertEqual(max_integer([42]), 42)

    def test_empty_list(self):
        """Test case for an empty list"""
        self.assertEqual(max_integer([]), None)

    def test_duplicate_values(self):
        """Test case for a list with duplicate values"""
        self.assertEqual(max_integer([1, 2, 2, 1]), 2)

    def test_mixed_positive_and_negative(self):
        """Test case for a list with both positive and negative numbers"""
        self.assertEqual(max_integer([1, -3, 2, -1, 0]), 2)

    def test_large_numbers(self):
        """Test case for a list with large numbers"""
        self.assertEqual(max_integer([1000000000, 999999999, 999999998]), 1000000000)

if __name__ == "__main__":
    unittest.main()
