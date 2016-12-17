import unittest
from Ip import Ip


class IpTest(unittest.TestCase):

    def test_ip_parser(self):
        ip = Ip()
        self.assertEquals(ip.parse("abba[mnop]qrst"), ["abba", "mnop", "qrst"])
        self.assertEquals(ip.parse("ioxxoj[asdfgh]zxcvbn"), ["ioxxoj", "asdfgh", "zxcvbn"])

    def test_abba(self):
        ip = Ip()
        self.assertEquals(ip.check_abba("abba"), True)
        self.assertEquals(ip.check_abba("abbb"), False)
        self.assertEquals(ip.check_abba("abaa"), False)
        self.assertEquals(ip.check_abba("aaaa"), False)
        self.assertEquals(ip.check_abba("cabbac"), True)
        self.assertEquals(ip.check_abba("ioxxoj"), True)
        self.assertEquals(ip.check_abba("hgfedcabbacdefgh"), True)

    def test_support_tls(self):
        ip = Ip()
        self.assertEquals(ip.support_tls("abba[mnop]qrst"), True)
        self.assertEquals(ip.support_tls("abcd[bddb]xyyx"), False)
        self.assertEquals(ip.support_tls("aaaa[qwer]tyui"), False)
        self.assertEquals(ip.support_tls("ioxxoj[asdfgh]zxcvbn"), True)
