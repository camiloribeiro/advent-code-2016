import unittest
from Taxicab import Taxicab


class TaxicabTest(unittest.TestCase):
    def test_get_to_headquarters(self):
        taxicab = Taxicab()
        self.assertEquals(taxicab.get_distance("R2, L3"), "R2, L3")

    def test_get_instructions_parsed(self):
        taxicab = Taxicab()
        self.assertEquals(taxicab.get_parsed_instructions("R2, L3"), [["R", 2], ["L", 3]])
        self.assertEquals(taxicab.get_parsed_instructions("R2, R2, R2"), [["R", 2], ["R", 2], ["R", 2]])
        self.assertEquals(taxicab.get_parsed_instructions("R5, L5, R5, R3"), [["R", 5], ["L", 5], ["R", 5], ["R", 3]])

    def test_parse_instruction(self):
        taxicab = Taxicab()
        self.assertEquals(taxicab.parse_instruction("R2"), ["R", 2])
        self.assertEquals(taxicab.parse_instruction(" R3"), ["R", 3])
        self.assertEquals(taxicab.parse_instruction("R5"), ["R", 5])
        self.assertEquals(taxicab.parse_instruction("   L3 "), ["L", 3])
        self.assertEquals(taxicab.parse_instruction("N22 "), ["N", 22])

    def test_get_direction(self):
        taxicab = Taxicab()
        self.assertEquals(taxicab.get_direction("N", "R"), "E")
        self.assertEquals(taxicab.get_direction("N", "L"), "W")
        self.assertEquals(taxicab.get_direction("W", "R"), "S")
        self.assertEquals(taxicab.get_direction("W", "L"), "N")
        self.assertEquals(taxicab.get_direction("E", "R"), "N")
        self.assertEquals(taxicab.get_direction("E", "L"), "S")
        self.assertEquals(taxicab.get_direction("S", "R"), "W")
        self.assertEquals(taxicab.get_direction("S", "L"), "E")

if __name__ == '__main__':
    unittest.main()
