import unittest
from Tfa import Tfa


class TfaTest(unittest.TestCase):

    def test_lighted_elements(self):
        tfa = Tfa()
        self.assertEqual(tfa.lighted_elements(), 0)

