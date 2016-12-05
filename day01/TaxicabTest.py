import unittest
from Taxicab import Taxicab


class TaxicabTest(unittest.TestCase):
    def test_get_to_headquarters(self):
        taxicab = Taxicab()
        self.assertEquals(taxicab.get_distance("R8, R4, R4, R8"), 4)
        self.assertEquals(taxicab.get_distance("R2, R2, R2, R8"), 0)
        self.assertEquals(taxicab.get_distance("R10, R2, R2, R8"), 8)
        self.assertEquals(taxicab.get_distance("R10, R2, R2, R1, R2"), 11)

    def test_get_instructions_parsed(self):
        taxicab = Taxicab()
        self.assertEquals(taxicab.get_parsed_instructions("R2, L3"), [["R", 2], ["L", 3]])
        self.assertEquals(taxicab.get_parsed_instructions("R2, R2, R2"), [["R", 2], ["R", 2], ["R", 2]])
        self.assertEquals(taxicab.get_parsed_instructions("R5, L5, R5, R3"), [["R", 5], ["L", 5], ["R", 5], ["R", 3]])

    def test_get_direction(self):
        taxicab = Taxicab()
        self.assertEquals(taxicab.get_direction("N", "R"), "E")
        self.assertEquals(taxicab.get_direction("N", "L"), "W")
        self.assertEquals(taxicab.get_direction("W", "R"), "N")
        self.assertEquals(taxicab.get_direction("W", "L"), "S")
        self.assertEquals(taxicab.get_direction("E", "R"), "S")
        self.assertEquals(taxicab.get_direction("E", "L"), "N")
        self.assertEquals(taxicab.get_direction("S", "R"), "W")
        self.assertEquals(taxicab.get_direction("S", "L"), "E")

if __name__ == '__main__':
    unittest.main()
