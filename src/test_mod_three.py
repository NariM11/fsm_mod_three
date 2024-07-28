"""
This module contains unit tests for the `mod_three` function defined in `src.mod_three`.

The `mod_three` function computes the remainder when a binary number (represented as a string) is divided by 3. The tests verify the correctness of this function through various cases, including:
- Basic binary strings of varying lengths.
- Long binary strings with a large number of ones.
- Binary strings with leading zeros.
- Edge cases such as empty strings and invalid inputs.
- Performance testing for very large binary strings.

The tests ensure that the function handles different input scenarios correctly and performs efficiently.
"""

import unittest
from src.mod_three import mod_three

class TestModThreeFSM(unittest.TestCase):

    def test_basic_cases(self):
        self.assertEqual(mod_three('1'), 1)
        self.assertEqual(mod_three('10'), 2)
        self.assertEqual(mod_three('11'), 0)
        self.assertEqual(mod_three('100'), 1)
        self.assertEqual(mod_three('1101'), 1)
        self.assertEqual(mod_three('1110'), 2)
        self.assertEqual(mod_three('1111'), 0)

    def test_long_binary_string(self):
        self.assertEqual(mod_three('1' * 1000), 0)
        self.assertEqual(mod_three('1' * 1001), 1)
        self.assertEqual(mod_three('10' * 1000), 2)

    def test_binary_string_with_leading_zeros(self):
        self.assertEqual(mod_three('000001101'), 1)
        self.assertEqual(mod_three('0000000'), 0)

    def test_empty_string(self):
        with self.assertRaises(ValueError):
            mod_three('')

    def test_invalid_input(self):
        with self.assertRaises(ValueError):
            mod_three('abc')
        with self.assertRaises(ValueError):
            mod_three('123')
        with self.assertRaises(ValueError):
            mod_three('1.1')
        with self.assertRaises(ValueError):
            mod_three(123)  # Test non-string input

    def test_performance(self):
        import time
        start_time = time.time()
        mod_three('1' * 1000000)
        end_time = time.time()
        self.assertTrue(end_time - start_time < 1)

if __name__ == '__main__':
    unittest.main()
