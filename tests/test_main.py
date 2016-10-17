# -*- coding: utf-8 -*-
import unittest

from basic_calculator import main


class TestBasicCalculator(unittest.TestCase):

    def test_simple(self):
        self.assertEqual(1 + 1, 2)
