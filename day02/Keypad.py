class Keypad:

    def __init__(self, keypad_instructions):
        self.directions = keypad_instructions

    def find_passcode(self, instructions):
        code = []
        for instruction in instructions.split("\n"):
            try:
                code.append(self.read_instruction(code[-1], instruction))
            except IndexError:
                code.append(self.read_instruction("5", instruction))
        return ''.join(map(str, code))

    def read_instruction(self, current, instructions):
        if not instructions:
            return current
        else:
            return self.read_instruction(
               self.get_position(current, list(instructions)[0]), instructions[1:])

    def get_position(self, current, instruction):
        try:
            return self.directions[current + instruction]
        except KeyError:
            return current
