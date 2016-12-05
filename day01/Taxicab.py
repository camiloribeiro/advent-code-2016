class Taxicab:

    def get_distance(self, directions):
        return directions

    def parse_instruction(self, instruction):
        return [instruction.strip()[0], int(instruction.strip()[1:])]
