# -*- coding: utf-8 -*-
import unittest

from basic_calculator import main


class TestBasicCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(basic_calculator(1, 7, 'add'), 8)

    def test_subtract(self):
        self.assertEqual(basic_calculator(5, 2, 'subtract'), 3)

    def test_multiply(self):
        self.assertEqual(basic_calculator(3, 4, 'multiply'), 12)

    def test_divide(self):
        self.assertEqual(basic_calculator(12, 3, 'divide'), 4)

    def test_invalid(self):
        self.assertEqual(basic_calculator(3, 4, 'what'), 'Invalid operation')
