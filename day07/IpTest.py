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

    def test_aba(self):
        ip = Ip()
        self.assertEquals(ip.check_aba(["aba", "asd"]), ["aba"])
        self.assertEquals(ip.check_aba(["abb", "asdd"]), [])
        self.assertEquals(ip.check_aba(["aaa"]), [])
        self.assertEquals(ip.check_aba(["cabcac"]), ["cac"])
        self.assertEquals(ip.check_aba(["ioxooj"]), ["oxo"])
        self.assertEquals(ip.check_aba(["hgfedcababcdefgh", "caci"]), ["aba", "bab", "cac"])

    def test_bab(self):
        ip = Ip()
        self.assertEquals(ip.check_bab(["bab"], ["aba"]), True)
        self.assertEquals(ip.check_bab(["bas", "foo", "bab"], ["aba"]), True)
        self.assertEquals(ip.check_bab(["bab"], ["abs", "asd", "aba"]), True)

    def test_support_tls(self):
        ip = Ip()
        self.assertEquals(ip.support_tls("abba[mnop]qrst"), True)
        self.assertEquals(ip.support_tls("abcd[bddb]xyyx"), False)
        self.assertEquals(ip.support_tls("aaaa[qwer]tyui"), False)
        self.assertEquals(ip.support_tls("ioxxoj[asdfgh]zxcvbn"), True)
        self.assertEquals(ip.support_tls("ioxxoj[asdfgh]zxcvbn[abba]asdggf"), False)

    def test_support_ssl(self):
        ip = Ip()
        self.assertEquals(ip.support_ssl("aba[bab]xyz"), True)
        self.assertEquals(ip.support_ssl("xyx[xyx]xyx"), False)
        self.assertEquals(ip.support_ssl("aaa[kek]eke"), True)
        self.assertEquals(ip.support_ssl("zazbz[bzb]cdb"), True)

    def test_count_tls_ips(self):
        ip = Ip()
        data = "abba[mnop]qrst\nabcd[bddb]xyyx\n" + \
               "aaaa[qwer]tyui\nioxxoj[asdfgh]zxcvbn"
        self.assertEquals(ip.count_tls_ips(data), 2)

    def test_count_ssl_ips(self):
        ip = Ip()
        data = "aba[bab]xyz\n" + \
               "aaaabaaaaaa[sad]xyz[asd]qwe[babababaab]ababababababadasdd\n" + \
               "aaa[sad]xyz[asd]qwe[ababa]aababa\n" + \
               "xyx[xyx]xyx\n" + \
               "aaa[kek]eke\n" + \
               "zazbz[bzb]cdb"
        self.assertEquals(ip.count_ssl_ips(data), 5)
