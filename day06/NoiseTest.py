import unittest
from Noise import Noise


class NoiseTest(unittest.TestCase):

    data = "eedadn\n" + \
            "drvtee\n" + \
            "eandsr\n" + \
            "raavrd\n" + \
            "atevrs\n" + \
            "tsrnev\n" + \
            "sdttsa\n" + \
            "rasrtv\n" + \
            "nssdts\n" + \
            "ntnada\n" + \
            "svetve\n" + \
            "tesnvt\n" + \
            "vntsnd\n" + \
            "vrdear\n" + \
            "dvrsen\n" + \
            "enarar"

    def test_get_message_with_most_repeated(self):
        noise = Noise()
        self.assertEquals(noise.get_message(self.data, 0), "easter")

    def test_get_message_with_least_repeated(self):
        noise = Noise()
        self.assertEquals(noise.get_message(self.data, -1), "advent")
