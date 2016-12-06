class Taxicab:

    def get_distance(self, instructions):
        towards, visited, distance = "N", [[0, 0]], {'N': 0, 'S': 0, 'E': 0, 'W': 0}
        directions = {'NL': 'W', 'SL': 'E', 'EL': 'N', 'WL': 'S',
                      'NR': 'E', 'SR': 'W', 'ER': 'S','WR': 'N'}
        for instruction in self.parse_instructions(instructions):
            towards = directions[towards + instruction[0]]
            for x in range(distance[towards], distance[towards] + instruction[1]):
                distance[towards] += 1
                x, y = distance['N'] - distance['S'], distance['W'] - distance['E']
                if [x, y] in visited:
                    return abs(x + y)
                visited.append([x, y])

    def parse_instructions(self, instructions):
        parsed_instructions = list()
        for instruction in instructions.split(","):
            parsed_instructions.append([instruction.strip()[0], int(instruction.strip()[1:])])
        return parsed_instructions
