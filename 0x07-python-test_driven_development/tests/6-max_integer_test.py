#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def setUp(self):
        self.data_1 = []
        self.data_2 = [5]
        self.data_3 = [1, 2, 3, 4]

    def test_max_integer(self):
        rslt_1 = max_integer(self.data_1)
        rslt_2 = max_integer(self.data_2)
        rslt_3 = max_integer(self.data_3)

        self.assertEqual(rslt_1, None)
        self.assertEqual(rslt_2, 5)
        self.assertEqual(rslt_3, 4)


if __name__ == '__main__':
    unittest.main()
