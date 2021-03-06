import unittest
from Decoy import Decoy


class DecoyTest(unittest.TestCase):

    def test_parse_room(self):
        decoy = Decoy()
        self.assertEquals(decoy.parse_room("room[checksum]"), ["room", "checksum"])

    def test_check_checksum(self):
        decoy = Decoy()
        self.assertEquals(decoy.check_checksum(["aaaaa-bbb-z-y-x-123", "abxyz"]), [123, 'aaaaa-bbb-z-y-x'])
        self.assertEquals(decoy.check_checksum(["a-b-c-d-e-f-g-h-987", "abcde"]), [987, 'a-b-c-d-e-f-g-h'])
        self.assertEquals(decoy.check_checksum(["not-a-real-room-404", "oarel"]), [404, 'not-a-real-room'])
        self.assertEquals(decoy.check_checksum(["totally-real-room-200", "decoy"]), [0])

    def test_get_total_sectors(self):
        decoy = Decoy()
        data = "aaaaa-bbb-z-y-x-123[abxyz]\n" + \
               "a-b-c-d-e-f-g-h-987[abcde]\n" + \
               "not-a-real-room-404[oarel]\n" + \
               "totally-real-room-200[decoy]"
        self.assertEquals(decoy.get_total_sectors(data), 1514)

    def test_get_all_valid_rooms(self):
        decoy = Decoy()
        data = "aaaaa-bbb-z-y-x-123[abxyz]\n" + \
               "a-b-c-d-e-f-g-h-987[abcde]\n" + \
               "not-a-real-room-404[oarel]\n" + \
               "totally-real-room-200[decoy]"

        valid_rooms = [[123, 'aaaaa-bbb-z-y-x'],
                       [987, 'a-b-c-d-e-f-g-h'],
                       [404, 'not-a-real-room']]

        self.assertEquals(decoy.get_all_valid_rooms(data), valid_rooms)

    def test_get_room_with_given_name(self):
        decoy = Decoy()
        data = "aaaaa-bbb-z-y-x-123[abxyz]\n" + \
               "a-b-c-d-e-f-g-h-987[abcde]\n" + \
               "not-a-real-room-404[oarel]\n" + \
               "totally-real-room-200[decoy]\n" + \
               "qzmt-zixmtkozy-ivhz-343[zimth]"
        self.assertEquals(decoy.get_room_with_given_name(data, "very encrypted name"), 343)

    def test_decode_room(self):
        decoy = Decoy()
        data = [343, "qzmt-zixmtkozy-ivhz"]
        self.assertEquals(decoy.decode_room(data), "very encrypted name")
