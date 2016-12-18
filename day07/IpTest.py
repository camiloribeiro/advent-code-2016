import unittest
from Ip import Ip


class IpTest(unittest.TestCase):

    def test_ip_parser_complex(self):
        ip = Ip()
        self.assertEquals(ip.parse("abba[mnop]qrst", [], []), [["abba", "qrst"], ["mnop"]])
        self.assertEquals(ip.parse("abcd[bddb]xyyx", [], []), [["abcd", "xyyx"], ["bddb"]])
        self.assertEquals(ip.parse("aaaa[qwer]tyui", [], []), [["aaaa", "tyui"], ["qwer"]])
        self.assertEquals(ip.parse("ioxxoj[asdfgh]zxcvbn", [], []), [["ioxxoj", "zxcvbn"], ["asdfgh"]])
        self.assertEquals(ip.parse("acca[qwer]qrst[tyui]xxsd", [], []), [["acca", "qrst", "xxsd"], ["qwer", "tyui"]])

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
        self.assertEquals(ip.support_tls("ioxxoj[asdfgh]zxcvbn[abba]asdggf"), False)

    def test_count_tls_ips(self):
        ip = Ip()
        data = "abba[mnop]qrst\nabcd[bddb]xyyx\n" + \
               "aaaa[qwer]tyui\nioxxoj[asdfgh]zxcvbn"
        self.assertEquals(ip.count_tls_ips(data), 2)
