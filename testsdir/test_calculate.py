import unittest
from calculate import calc
import math

class TestCalc(unittest.TestCase):

    def test_circle_area(self):
        result = calc('circle', 'area', [5])
        expected = math.pi * 5 ** 2
        self.assertAlmostEqual(result, expected, places=5)

    def test_square_perimeter(self):
        result = calc('square', 'perimeter', [4])
        expected = 4 * 4
        self.assertEqual(result, expected)

    def test_invalid_figure(self):
        with self.assertRaises(AssertionError):
            calc('triangle', 'area', [3, 4, 5])

    def test_invalid_function(self):
        with self.assertRaises(AssertionError):
            calc('circle', 'volume', [3])

    def test_invalid_size(self):
        with self.assertRaises(TypeError):
            calc('circle', 'area', [3, 4])

if __name__ == '__main__':
    unittest.main()
