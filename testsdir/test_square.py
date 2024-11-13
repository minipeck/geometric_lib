import unittest
from square import area, perimeter


class TestSquareFunctions(unittest.TestCase):

    def test_area_positive(self):
        self.assertEqual(area(5), 25)

    def test_area_zero(self):
        self.assertEqual(area(0), 0)

    def test_area_negative(self):
        with self.assertRaises(ValueError):
            area(-5)

    def test_perimeter_positive(self):
        self.assertEqual(perimeter(5), 20)

    def test_perimeter_zero(self):
        self.assertEqual(perimeter(0), 0)

    def test_perimeter_negative(self):
        with self.assertRaises(ValueError):
            perimeter(-5)


if __name__ == "__main__":
    unittest.main()
