class Taxicab:

    def get_distance(self, directions):
        distance = {'N': 0, 'S': 0, 'E': 0, 'W': 0}
        towards = "N"
        visited = [[0, 0]]
        
        instructions = self.get_parsed_instructions(directions)
        for instruction in instructions:
            towards = self.get_direction(towards, instruction[0])
            for x in range(distance[towards], distance[towards] + instruction[1]):
                distance[towards] += 1
                x = distance['N'] - distance['S']
                y = distance['W'] - distance['E']
                if [x, y] in visited:
                    return abs(y + x)
                else:
                    visited.append([x, y])

    def get_parsed_instructions(self, instructions):
        parsed_instructions = list()
        for instruction in instructions.split(","):
            parsed_instructions.append([instruction.strip()[0], int(instruction.strip()[1:])])
        return parsed_instructions

    def get_direction(self, current_towards, direction):
        options = {'NL': 'W',
                   'SL': 'E',
                   'EL': 'N',
                   'WL': 'S',
                   'NR': 'E',
                   'SR': 'W',
                   'ER': 'S',
                   'WR': 'N'}
        return options[current_towards + direction]
