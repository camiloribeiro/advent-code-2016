import unittest
from Tfa import Tfa


class TfaTest(unittest.TestCase):

    def test_lighted_elements(self):
        tfa = Tfa()
        self.assertEqual(tfa.lighted_elements(), 0)

    def test_rect(self):
        tfa = Tfa()
        display = [[0 for x in range(7)] for y in range(3)]
        self.assertEquals(tfa.rect([2, 3], display), [[1, 1, 1, 0, 0, 0, 0],
                                                      [1, 1, 1, 0, 0, 0, 0],
                                                      [0, 0, 0, 0, 0, 0, 0]])

    def test_rotate_column(self):
        tfa = Tfa()
        display = [[0 for x in range(7)] for y in range(3)]
        display = tfa.rect([2, 3], display)
        self.assertEquals(tfa.rotate_col([1, 1], display), [[1, 0, 1, 0, 0, 0, 0],
                                                            [1, 1, 1, 0, 0, 0, 0],
                                                            [0, 1, 0, 0, 0, 0, 0]])

    def test_rotate_column_overflow(self):
        tfa = Tfa()
        display = [[0 for x in range(7)] for y in range(3)]
        display = tfa.rect([2, 3], display)
        self.assertEqual(tfa.rotate_col([1, 2], display), [[1, 1, 1, 0, 0, 0, 0],
                                                           [1, 0, 1, 0, 0, 0, 0],
                                                           [0, 1, 0, 0, 0, 0, 0]])

    def test_column_column(self):
        tfa = Tfa()
        display = [[0 for x in range(7)] for y in range(3)]
        display = tfa.rect([2, 3], display)
        display = tfa.rotate_col([1, 1], display)
        self.assertItemsEqual(tfa.rotate_row(0, 4, display), [[0, 0, 0, 0, 1, 0, 1],
                                                              [1, 1, 1, 0, 0, 0, 0],
                                                              [0, 1, 0, 0, 0, 0, 0]])

    def test_parse_input_rect(self):
        tfa = Tfa()
        display = [[0 for x in range(7)] for y in range(3)]
        data = "rect 2x3"
        self.assertEquals(tfa.parse_input(data, display), [[1, 1, 1, 0, 0, 0, 0],
                                                           [1, 1, 1, 0, 0, 0, 0],
                                                           [0, 0, 0, 0, 0, 0, 0]])

    def test_parse_input_col(self):
        tfa = Tfa()
        display = [[0 for x in range(7)] for y in range(3)]
        data = "rect 2x3\n" + \
              "rotate column x=1 by 1"
        self.assertEquals(tfa.parse_input(data, display), [[1, 0, 1, 0, 0, 0, 0],
                                                           [1, 1, 1, 0, 0, 0, 0],
                                                           [0, 1, 0, 0, 0, 0, 0]])
#
#    def test_parse_input_row(self):
#        tfa = Tfa()
#        display = [[0 for x in range(7)] for y in range(3)]
#        data = "rect 2x3"
#        self.assertEquals(tfa.parse_input(data, display), [[1, 1, 1, 0, 0, 0, 0],
#                                                           [1, 1, 1, 0, 0, 0, 0],
#                                                           [0, 0, 0, 0, 0, 0, 0]])
