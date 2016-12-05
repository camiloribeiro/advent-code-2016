import unittest
from Taxicab import Taxicab


class TaxicabTest(unittest.TestCase):
    def test_get_to_headquarters(self):
        taxicab = Taxicab()
        self.assertEquals(taxicab.get_distance("R2, L3"), "R2, L3")

if __name__ == '__main__':
    unittest.main()
