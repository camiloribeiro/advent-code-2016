import unittest
from Noise import Noise


class NoiseTest(unittest.TestCase):

    def test_get_most_repeated_chat(self):
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
        self.assertEquals(noise.get_most_repeated_char(data), "easter")

if __name__ == '__main__':
    unittest.main()
