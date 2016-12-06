import unittest
from ThreeSides import ThreeSides


class ThreeSidesTest(unittest.TestCase):

    def test_is_triangle(self):
        # My blog post from 2010 http://www.bugbang.com.br/uma-introducao-a-tdd-com-junit/
        three_sides = ThreeSides()
        self.assertEquals(three_sides.is_a_valid_triangle(3, 4, 5), True)
        self.assertEquals(three_sides.is_a_valid_triangle(5, 10, 25), False)
        self.assertEquals(three_sides.is_a_valid_triangle(2, 9, 10), True)
        self.assertEquals(three_sides.is_a_valid_triangle(20, 20, 20), True)
        self.assertEquals(three_sides.is_a_valid_triangle(20, 20, 30), True)
        self.assertEquals(three_sides.is_a_valid_triangle(20, 30, 20), True)
        self.assertEquals(three_sides.is_a_valid_triangle(30, 20, 20), True)
        self.assertEquals(three_sides.is_a_valid_triangle(0, 2, 9), False)
        self.assertEquals(three_sides.is_a_valid_triangle(3, -2, 9), False)
        self.assertEquals(three_sides.is_a_valid_triangle(5, 6, 11), False)
        self.assertEquals(three_sides.is_a_valid_triangle(5, 11, 6), False)
        self.assertEquals(three_sides.is_a_valid_triangle(11, 6, 5), False)
        self.assertEquals(three_sides.is_a_valid_triangle(5, 6, 12), False)
        self.assertEquals(three_sides.is_a_valid_triangle(0, 0, 0), False)
        self.assertEquals(three_sides.is_a_valid_triangle(5, 12, 6), False)
        self.assertEquals(three_sides.is_a_valid_triangle(12, 5, 6), False)

if __name__ == '__main__':
    unittest.main()
