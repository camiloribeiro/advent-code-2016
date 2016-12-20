import unittest
from Tfa import Tfa


class TfaTest(unittest.TestCase):

    def test_lighted_elements(self):
        tfa = Tfa()
        self.assertEqual(tfa.lighted_elements(), 0)

    def test_react(self):
        tfa = Tfa()
        display = [[0 for x in range(7)] for y in range(3)]
        self.assertItemsEqual(tfa.react(2, 3, display), [[1, 1, 1, 0, 0, 0, 0],
                                                         [1, 1, 1, 0, 0, 0, 0],
                                                         [0, 0, 0, 0, 0, 0, 0]])

    def test_rotate_column(self):
        tfa = Tfa()
        display = [[0 for x in range(7)] for y in range(3)]
        display = tfa.react(2, 3, display)
        self.assertItemsEqual(tfa.rotate_col(1, 1, display), [[1, 0, 1, 0, 0, 0, 0],
                                                              [1, 1, 1, 0, 0, 0, 0],
                                                              [0, 1, 0, 0, 0, 0, 0]])

    def test_rotate_column_overflow(self):
        tfa = Tfa()
        display = [[0 for x in range(7)] for y in range(3)]
        display = tfa.react(2, 3, display)
        self.assertItemsEqual(tfa.rotate_col(1, 2, display), [[1, 1, 1, 0, 0, 0, 0],
                                                              [1, 0, 1, 0, 0, 0, 0],
                                                              [0, 1, 0, 0, 0, 0, 0]])
