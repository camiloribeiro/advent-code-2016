import unittest
from Keypad import Keypad


class KeypadTest(unittest.TestCase):

    layout1 = {'5U': '2', '5D': '8', '5L': '4', '5R': '6',
               '2D': '5', '2L': '1', '2R': '3',
               '4U': '1', '4D': '7', '4R': '5',
               '6U': '3', '6D': '9', '6L': '5',
               '8U': '5', '8L': '7', '8R': '9',
               '1D': '4', '1R': '2',
               '3D': '6', '3L': '2',
               '7U': '4', '7R': '8',
               '9U': '6', '9L': '8'}

    def test_find_passcode(self):
        keypad = Keypad(self.layout1)

        instructions = "ULL\n" + \
                       "RRDDD\n" + \
                       "LURDL\n" + \
                       "UUUUD"
        self.assertEquals(keypad.find_passcode(instructions), "1985")

    def test_read_instruction(self):
        keypad = Keypad(self.layout1)

        self.assertEquals(keypad.read_instruction("5", "U"), "2")
        self.assertEquals(keypad.read_instruction("5", "ULL"), "1")
        self.assertEquals(keypad.read_instruction("1", "RRDDD"), "9")
        self.assertEquals(keypad.read_instruction("9", "LURDL"), "8")
        self.assertEquals(keypad.read_instruction("8", "UUUUD"), "5")

    def test_get_position(self):

        keypad = Keypad(self.layout1)

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
