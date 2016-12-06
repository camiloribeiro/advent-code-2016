import unittest
from ThreeSides import ThreeSides


class ThreeSidesTest(unittest.TestCase):

    def test_is_triangle(self):
        three_sides = ThreeSides()
        self.assertEquals(three_sides.is_a_valid_triangle(3, 4, 5), True)

if __name__ == '__main__':
    unittest.main()
