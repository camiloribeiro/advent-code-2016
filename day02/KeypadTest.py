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

    layout2 = {'5R': '6',
               '1D': '3',
               '9L': '8',
               'DU': 'B',
               '2R': '3', '2D': '6',
               '4L': '3', '4D': '8',
               'AR': 'B', 'AU': '6',
               'CL': 'B', 'CU': '8',
               '3D': '7', '3U': '1', '3L': '2', '3R': '4',
               '8D': 'C', '8U': '4', '8L': '7', '8R': '9',
               '6D': 'A', '6U': '2', '6L': '5', '6R': '7',
               'BD': 'D', 'BU': '7', 'BL': 'A', 'BR': 'C',
               '7D': 'B', '7U': '3', '7L': '6', '7R': '8'}

    def test_find_passcode(self):
        keypad = Keypad()

        instructions = "ULL\n" + \
                       "RRDDD\n" + \
                       "LURDL\n" + \
                       "UUUUD"
        self.assertEquals(keypad.find_passcode(self.layout1, instructions), "1985")
        self.assertEquals(keypad.find_passcode(self.layout2, instructions), "5DB3")

    def test_read_instruction(self):
        keypad = Keypad()

        self.assertEquals(keypad.read_instruction(self.layout1, "5", "U"), "2")
        self.assertEquals(keypad.read_instruction(self.layout1, "5", "ULL"), "1")
        self.assertEquals(keypad.read_instruction(self.layout1, "1", "RRDDD"), "9")
        self.assertEquals(keypad.read_instruction(self.layout1, "9", "LURDL"), "8")
        self.assertEquals(keypad.read_instruction(self.layout1, "8", "UUUUD"), "5")

        self.assertEquals(keypad.read_instruction(self.layout2, "5", "U"), "5")
        self.assertEquals(keypad.read_instruction(self.layout2, "5", "ULL"), "5")
        self.assertEquals(keypad.read_instruction(self.layout2, "5", "RRDDD"), "D")
        self.assertEquals(keypad.read_instruction(self.layout2, "D", "LURDL"), "B")
        self.assertEquals(keypad.read_instruction(self.layout2, "3", "UUUUD"), "3")

    def test_get_position_layout_1(self):

        keypad = Keypad()

        self.assertEquals(keypad.get_position(self.layout1, "1", "U"), "1")
        self.assertEquals(keypad.get_position(self.layout1, "1", "D"), "4")
        self.assertEquals(keypad.get_position(self.layout1, "1", "L"), "1")
        self.assertEquals(keypad.get_position(self.layout1, "1", "R"), "2")

        self.assertEquals(keypad.get_position(self.layout1, "2", "U"), "2")
        self.assertEquals(keypad.get_position(self.layout1, "2", "D"), "5")
        self.assertEquals(keypad.get_position(self.layout1, "2", "L"), "1")
        self.assertEquals(keypad.get_position(self.layout1, "2", "R"), "3")

        self.assertEquals(keypad.get_position(self.layout1, "3", "U"), "3")
        self.assertEquals(keypad.get_position(self.layout1, "3", "D"), "6")
        self.assertEquals(keypad.get_position(self.layout1, "3", "L"), "2")
        self.assertEquals(keypad.get_position(self.layout1, "3", "R"), "3")

        self.assertEquals(keypad.get_position(self.layout1, "4", "U"), "1")
        self.assertEquals(keypad.get_position(self.layout1, "4", "D"), "7")
        self.assertEquals(keypad.get_position(self.layout1, "4", "L"), "4")
        self.assertEquals(keypad.get_position(self.layout1, "4", "R"), "5")

        self.assertEquals(keypad.get_position(self.layout1, "5", "U"), "2")
        self.assertEquals(keypad.get_position(self.layout1, "5", "D"), "8")
        self.assertEquals(keypad.get_position(self.layout1, "5", "L"), "4")
        self.assertEquals(keypad.get_position(self.layout1, "5", "R"), "6")

        self.assertEquals(keypad.get_position(self.layout1, "6", "U"), "3")
        self.assertEquals(keypad.get_position(self.layout1, "6", "D"), "9")
        self.assertEquals(keypad.get_position(self.layout1, "6", "L"), "5")
        self.assertEquals(keypad.get_position(self.layout1, "6", "R"), "6")

        self.assertEquals(keypad.get_position(self.layout1, "7", "U"), "4")
        self.assertEquals(keypad.get_position(self.layout1, "7", "D"), "7")
        self.assertEquals(keypad.get_position(self.layout1, "7", "L"), "7")
        self.assertEquals(keypad.get_position(self.layout1, "7", "R"), "8")

        self.assertEquals(keypad.get_position(self.layout1, "8", "U"), "5")
        self.assertEquals(keypad.get_position(self.layout1, "8", "D"), "8")
        self.assertEquals(keypad.get_position(self.layout1, "8", "L"), "7")
        self.assertEquals(keypad.get_position(self.layout1, "8", "R"), "9")

        self.assertEquals(keypad.get_position(self.layout1, "9", "U"), "6")
        self.assertEquals(keypad.get_position(self.layout1, "9", "D"), "9")
        self.assertEquals(keypad.get_position(self.layout1, "9", "L"), "8")
        self.assertEquals(keypad.get_position(self.layout1, "9", "R"), "9")

if __name__ == '__main__':
    unittest.main()
