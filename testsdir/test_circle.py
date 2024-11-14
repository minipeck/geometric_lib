import unittest
from circle import area, perimeter


class TestCircleFunctions(unittest.TestCase):

    def test_area_positive(self):
        self.assertAlmostEqual(area(8), 201.06192982974676)

    def test_area_zero(self):
        self.assertEqual(area(0), 0)

    def test_area_negative(self):
        with self.assertRaises(ValueError):
            area(-5)

    def test_perimeter_positive(self):
        self.assertAlmostEqual(perimeter(8), 50.26548245743669)

    def test_perimeter_zero(self):
        self.assertEqual(perimeter(0), 0)

    def test_perimeter_negative(self):
        with self.assertRaises(ValueError):
            perimeter(-5)


if __name__ == "__main__":
    unittest.main()
