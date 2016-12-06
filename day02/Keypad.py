class Keypad:

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
        directions = {'5U': '2', '5D': '8', '5L': '4', '5R': '6',
                      '2D': '5', '2L': '1', '2R': '3',
                      '4U': '1', '4D': '7', '4R': '5',
                      '6U': '3', '6D': '9', '6L': '5',
                      '8U': '5', '8L': '7', '8R': '9',
                      '1D': '4', '1R': '2',
                      '3D': '6', '3L': '2',
                      '7U': '4', '7R': '8',
                      '9U': '6', '9L': '8'}
        try:
            return directions[current + instruction]
        except KeyError:
            return current
