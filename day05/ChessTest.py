import unittest
from Chess import Chess


class ChessTest(unittest.TestCase):

    def test_get_password(self):
        chess = Chess()
        self.assertEquals(chess.get_simple_password("abc"), "18f47a30")

    def test_get_enhanced_password(self):
        chess = Chess()
        self.assertEquals(chess.get_enhanced_password("abc"), "05ace8e3")
