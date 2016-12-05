class Taxicab:

    def get_distance(self, directions):
        return directions

    def get_parsed_instructions(self, instructions):
        parsed_instructions = list()
        for instruction in instructions.split(","):
            parsed_instructions.append(self.parse_instruction(instruction))
        return parsed_instructions

    def parse_instruction(self, instruction):
        return [instruction.strip()[0], int(instruction.strip()[1:])]
