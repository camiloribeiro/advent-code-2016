import unittest
from Decoy import Decoy


class DecoyTest(unittest.TestCase):

    def test_parse_room(self):
        decoy = Decoy()
        self.assertEquals(decoy.parse_room("room[checksum]"), ["room", "checksum"])

    def test_check_checksum(self):
        decoy = Decoy()
        self.assertEquals(decoy.check_checksum(["aaaaa-bbb-z-y-x-123", "abxyz"]), 123)
        self.assertEquals(decoy.check_checksum(["a-b-c-d-e-f-g-h-987", "abcde"]), 987)
        self.assertEquals(decoy.check_checksum(["not-a-real-room-404", "oarel"]), 404)
        self.assertEquals(decoy.check_checksum(["totally-real-room-200", "decoy"]), False)

    def test_get_total_sectors(self):
        decoy = Decoy()
        data = "aaaaa-bbb-z-y-x-123[abxyz]\n" + \
               "a-b-c-d-e-f-g-h-987[abcde]\n" + \
               "not-a-real-room-404[oarel]\n" + \
               "totally-real-room-200[decoy]"
        self.assertEquals(decoy.get_total_sectors(data), 1514)

    def test_decode_room(self):
        decoy = Decoy()
        data = "qzmt-zixmtkozy-ivhz-343"
        self.assertEquals(decoy.decode_room(data), "very encrypted name")

if __name__ == '__main__':
    unittest.main()
