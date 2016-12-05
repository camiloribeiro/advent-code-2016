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

    def get_direction(self, current_towards, direction):
        if current_towards == "N":
            if direction == "L":
                return "W"
            if direction == "R":
                return "E"
        if current_towards == "S":
            if direction == "L":
                return "E"
            if direction == "R":
                return "W"
        if current_towards == "E":
            if direction == "L":
                return "N"
            if direction == "R":
                return "S"
        if current_towards == "W":
            if direction == "L":
                return "S"
            if direction == "R":
                return "N"
