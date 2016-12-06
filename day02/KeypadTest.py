import unittest
from Keypad import Keypad


class KeypadTest(unittest.TestCase):

    def test_read_instruction(self):
        keypad = Keypad()
        self.assertEquals(keypad.read_instruction("5", "U"), "2")
        self.assertEquals(keypad.read_instruction("5", "ULL"), "1")
        self.assertEquals(keypad.read_instruction("1", "RRDDD"), "9")
        self.assertEquals(keypad.read_instruction("9", "LURDL"), "8")
        self.assertEquals(keypad.read_instruction("8", "UUUUD"), "5")

    def test_get_position(self):
        keypad = Keypad()

        self.assertEquals(keypad.get_position("1", "U"), "1")
        self.assertEquals(keypad.get_position("1", "D"), "4")
        self.assertEquals(keypad.get_position("1", "L"), "1")
        self.assertEquals(keypad.get_position("1", "R"), "2")
        
        self.assertEquals(keypad.get_position("2", "U"), "2")
        self.assertEquals(keypad.get_position("2", "D"), "5")
        self.assertEquals(keypad.get_position("2", "L"), "1")
        self.assertEquals(keypad.get_position("2", "R"), "3")

        self.assertEquals(keypad.get_position("3", "U"), "3")
        self.assertEquals(keypad.get_position("3", "D"), "6")
        self.assertEquals(keypad.get_position("3", "L"), "2")
        self.assertEquals(keypad.get_position("3", "R"), "3")

        self.assertEquals(keypad.get_position("4", "U"), "1")
        self.assertEquals(keypad.get_position("4", "D"), "7")
        self.assertEquals(keypad.get_position("4", "L"), "4")
        self.assertEquals(keypad.get_position("4", "R"), "5")

        self.assertEquals(keypad.get_position("5", "U"), "2")
        self.assertEquals(keypad.get_position("5", "D"), "8")
        self.assertEquals(keypad.get_position("5", "L"), "4")
        self.assertEquals(keypad.get_position("5", "R"), "6")

        self.assertEquals(keypad.get_position("6", "U"), "3")
        self.assertEquals(keypad.get_position("6", "D"), "9")
        self.assertEquals(keypad.get_position("6", "L"), "5")
        self.assertEquals(keypad.get_position("6", "R"), "6")

        self.assertEquals(keypad.get_position("7", "U"), "4")
        self.assertEquals(keypad.get_position("7", "D"), "7")
        self.assertEquals(keypad.get_position("7", "L"), "7")
        self.assertEquals(keypad.get_position("7", "R"), "8")

        self.assertEquals(keypad.get_position("8", "U"), "5")
        self.assertEquals(keypad.get_position("8", "D"), "8")
        self.assertEquals(keypad.get_position("8", "L"), "7")
        self.assertEquals(keypad.get_position("8", "R"), "9")

        self.assertEquals(keypad.get_position("9", "U"), "6")
        self.assertEquals(keypad.get_position("9", "D"), "9")
        self.assertEquals(keypad.get_position("9", "L"), "8")
        self.assertEquals(keypad.get_position("9", "R"), "9")

if __name__ == '__main__':
    unittest.main()
