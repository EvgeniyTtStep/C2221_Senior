import unittest
from lesson8 import adder

class MyTest(unittest.TestCase):

    def test_args(self):
        self.assertEqual(4, adder(2,3))

    def test_args_negative(self):
        self.assertEqual(-6, adder(-2,-3))