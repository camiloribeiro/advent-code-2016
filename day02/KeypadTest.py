import unittest
from Keypad import Keypad


class KeypadTest(unittest.TestCase):

    def test_read_instruction(self):
        keypad = Keypad()
        self.assertEquals(keypad.read_instruction("U"), "U")

if __name__ == '__main__':
    unittest.main()
