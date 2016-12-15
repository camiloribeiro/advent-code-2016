import unittest
from Keypad import Keypad
from KeypadLayouts import KeypadLayouts


class KeypadTest(unittest.TestCase):

    def test_find_passcode(self):
        keypad = Keypad()

        instructions = "ULL\n" + \
                       "RRDDD\n" + \
                       "LURDL\n" + \
                       "UUUUD"
        self.assertEquals(keypad.find_passcode(KeypadLayouts.layout1, instructions), "1985")
        self.assertEquals(keypad.find_passcode(KeypadLayouts.layout2, instructions), "5DB3")

    def test_read_instruction(self):
        keypad = Keypad()

        self.assertEquals(keypad.read_instruction(KeypadLayouts.layout1, "5", "U"), "2")
        self.assertEquals(keypad.read_instruction(KeypadLayouts.layout1, "5", "ULL"), "1")
        self.assertEquals(keypad.read_instruction(KeypadLayouts.layout1, "1", "RRDDD"), "9")
        self.assertEquals(keypad.read_instruction(KeypadLayouts.layout1, "9", "LURDL"), "8")
        self.assertEquals(keypad.read_instruction(KeypadLayouts.layout1, "8", "UUUUD"), "5")

        self.assertEquals(keypad.read_instruction(KeypadLayouts.layout2, "5", "U"), "5")
        self.assertEquals(keypad.read_instruction(KeypadLayouts.layout2, "5", "ULL"), "5")
        self.assertEquals(keypad.read_instruction(KeypadLayouts.layout2, "5", "RRDDD"), "D")
        self.assertEquals(keypad.read_instruction(KeypadLayouts.layout2, "D", "LURDL"), "B")
        self.assertEquals(keypad.read_instruction(KeypadLayouts.layout2, "3", "UUUUD"), "3")
