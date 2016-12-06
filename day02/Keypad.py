class Keypad:

    def find_passcode(self, layout, instructions):
        code = []
        for instruction in instructions.split("\n"):
            try:
                code.append(self.read_instruction(layout, code[-1], instruction))
            except IndexError:
                code.append(self.read_instruction(layout, "5", instruction))
        return ''.join(map(str, code))

    def read_instruction(self, layout, current, instructions):
        if not instructions:
            return current
        else:
            return self.read_instruction(
               layout, self.get_position(layout, current, list(instructions)[0]), instructions[1:])

    def get_position(self, layout, current, instruction):
        try:
            return layout[current + instruction]
        except KeyError:
            return current
