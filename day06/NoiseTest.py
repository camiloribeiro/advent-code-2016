import unittest
from Noise import Noise


class NoiseTest(unittest.TestCase):

    def test_get_message_with_most_repeated(self):
        noise = Noise()
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
        self.assertEquals(noise.get_message(data, 0), "easter")

    def test_get_message_with_least_repeated(self):
        noise = Noise()
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
        self.assertEquals(noise.get_message(data, -1), "advent")
