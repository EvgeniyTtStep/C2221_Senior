import unittest
from lesson8 import adder,sum

class MyTest(unittest.TestCase):

    def test_args(self):
        self.assertEqual(4, adder(2,3))

    def test_args_negative(self):
        self.assertEqual(-6, adder(-2,-3))

    def test_sum(self):
        self.assertEqual(5, sum(2, 2))

    def test_sum_zero(self):
        self.assertEqual(1, sum(0, 0))