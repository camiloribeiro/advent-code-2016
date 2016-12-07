import unittest
from Decoy import Decoy


class DecoyTest(unittest.TestCase):

    def test_parse_room(self):
        decoy = Decoy()
        self.assertEquals(decoy.parse_room("room[checksum]"), ["room", "checksum"])

if __name__ == '__main__':
    unittest.main()
