import unittest
from Ip import Ip


class IpTest(unittest.TestCase):

    def test_ip_parser(self):
        ip = Ip()
        self.assertEquals(ip.parse("abba[mnop]qrst"), ["abba", "mnop", "qrst"])
