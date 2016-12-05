import unittest
from Taxicab import Taxicab


class TaxicabTest(unittest.TestCase):
    def test_get_to_headquarters(self):
        taxicab = Taxicab()
        self.assertEquals(taxicab.get_distance("R8, R4, R4, R8"), 4)
        self.assertEquals(taxicab.get_distance("R2, R2, R2, R8"), 0)
        self.assertEquals(taxicab.get_distance("R10, R2, R2, R8"), 8)
        self.assertEquals(taxicab.get_distance("R10, R2, R2, R1, R2"), 11)

    def test_parse_instructions(self):
        taxicab = Taxicab()
        self.assertEquals(taxicab.parse_instructions("R2, L3"), [["R", 2], ["L", 3]])
        self.assertEquals(taxicab.parse_instructions("R2, R2, R2"), [["R", 2], ["R", 2], ["R", 2]])
        self.assertEquals(taxicab.parse_instructions("R5, L5, R5, R3"), [["R", 5], ["L", 5], ["R", 5], ["R", 3]])

if __name__ == '__main__':
    unittest.main()
