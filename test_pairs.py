import unittest
import os
from pairs import *

class TestFindPairs(unittest.TestCase):
    print()

    def test_happy_path(self):  
        input = [0, 1, 2, 5, 9, 10, 12]
        expected_output = [(0, 12),(2, 10)]
        actual_output = find_pairs(input)
        self.assertAlmostEqual(actual_output, expected_output)

    def test_no_match_found(self):
        input = [1, 12]
        expected_output = []
        actual_output = find_pairs(input)
        self.assertAlmostEqual(actual_output, expected_output)

    def test_multiple_same_int_pairs(self):
        input = [0, 1, 2, 3, 6, 6, 6, 6, 12, 5, 7]
        expected_output = [(0, 12),(5, 7),(6, 6)]
        actual_output = find_pairs(input)
        self.assertAlmostEqual(actual_output, expected_output)

    def test_single_element_list(self):
        input = [1]
        expected_output = []
        actual_output = find_pairs(input)
        self.assertAlmostEqual(actual_output, expected_output)
    
    def test_element_above_sum_to(self):
        input = [1, 11, 1200, 5]
        with self.assertRaises(AssertionError):
            find_pairs(input)

    def test_empty_list(self):
        with self.assertRaises(AssertionError):
            find_pairs([])

    def test_list_is_none(self):
        with self.assertRaises(AssertionError):
            find_pairs(None)

    def test_list_element_below_zero(self):
        with self.assertRaises(AssertionError):
            find_pairs([1, 2, 5, -1, 11])

    def test_char_in_list(self):
        with self.assertRaises(TypeError):
            input = [1, 12, "s", 11]
            find_pairs(input)

    def test_float_in_list(self):
        with self.assertRaises(TypeError):
            input = [1, 12, 3.5, 9]
            find_pairs(input)

    def test_list_in_a_list(self):
        with self.assertRaises(TypeError):
            input = [1, 11, [2,10], 5]
            find_pairs(input)

if __name__ == '__main__':
    unittest.main(verbosity=2)
