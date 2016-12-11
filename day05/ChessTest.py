import unittest
from Chess import Chess


class ChessTest(unittest.TestCase):

    def test_get_key_for_character(self):
        chess = Chess()
        self.assertEquals(chess.get_key_for_character("abc"), "1")

if __name__ == '__main__':
    unittest.main()
