import unittest
from Taxicab import Taxicab


class TaxicabTest(unittest.TestCase):
    def test_get_to_headquarters(self):
        taxicab = Taxicab()
        self.assertEquals(taxicab.get_distance("R2, L3"), "R2, L3")

    def test_parse_instruction(self):
        taxicab = Taxicab()
        self.assertEquals(taxicab.parse_instruction("R2"), ["R", 2])
        self.assertEquals(taxicab.parse_instruction("R3"), ["R", 3])
        self.assertEquals(taxicab.parse_instruction("R5"), ["R", 5])
        self.assertEquals(taxicab.parse_instruction("L3"), ["L", 3])
        self.assertEquals(taxicab.parse_instruction("N22"), ["N", 22])

if __name__ == '__main__':
    unittest.main()
