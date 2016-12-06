import unittest
from ThreeSides import ThreeSides


class ThreeSidesTest(unittest.TestCase):

    def test_is_triangle(self):
        # My blog post from 2010 http://www.bugbang.com.br/uma-introducao-a-tdd-com-junit/
        three_sides = ThreeSides()
        self.assertEquals(three_sides.is_a_valid_triangle([3, 4, 5]), True)
        self.assertEquals(three_sides.is_a_valid_triangle([5, 10, 25]), False)
        self.assertEquals(three_sides.is_a_valid_triangle([2, 9, 10]), True)
        self.assertEquals(three_sides.is_a_valid_triangle([20, 20, 20]), True)
        self.assertEquals(three_sides.is_a_valid_triangle([20, 20, 30]), True)
        self.assertEquals(three_sides.is_a_valid_triangle([20, 30, 20]), True)
        self.assertEquals(three_sides.is_a_valid_triangle([30, 20, 20]), True)
        self.assertEquals(three_sides.is_a_valid_triangle([0, 2, 9]), False)
        self.assertEquals(three_sides.is_a_valid_triangle([3, -2, 9]), False)
        self.assertEquals(three_sides.is_a_valid_triangle([5, 6, 11]), False)
        self.assertEquals(three_sides.is_a_valid_triangle([5, 11, 6]), False)
        self.assertEquals(three_sides.is_a_valid_triangle([11, 6, 5]), False)
        self.assertEquals(three_sides.is_a_valid_triangle([5, 6, 12]), False)
        self.assertEquals(three_sides.is_a_valid_triangle([0, 0, 0]), False)
        self.assertEquals(three_sides.is_a_valid_triangle([5, 12, 6]), False)
        self.assertEquals(three_sides.is_a_valid_triangle([12, 5, 6]), False)

    def test_get_number_of_valid_triangles(self):
        three_sides = ThreeSides()
        self.assertEquals(three_sides.get_valid_triangles("   3     4    5\n" +
                                                          "   5    10    25\n" +
                                                          "   2     9    10\n" +
                                                          "  20    20    20\n" +
                                                          "  20    20    30\n" +
                                                          "  20    30    20\n" +
                                                          "  30    20    20\n" +
                                                          "   0     2    9\n" +
                                                          "   3    -2    9\n" +
                                                          "   5     6    11\n" +
                                                          "   5    11    6\n" +
                                                          "  11    6    5\n" +
                                                          "   5     6    12\n" +
                                                          "   0     0    0\n" +
                                                          "   5    12    6\n" +
                                                          "  12    5    6"), 6)

if __name__ == '__main__':
    unittest.main()
