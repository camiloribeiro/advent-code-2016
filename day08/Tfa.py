import re


class Tfa:
    def lighted_elements(self):
        display, lighted = [[0 for x in range(50)] for y in range(8)], 0
        for row in range(len(display)):
            for col in range(len(display[0])):
                lighted += display[row][col]
        return lighted

    def rect(self, hw, display):
        for row in range(0, hw[0]):
            for col in range(0, hw[1]):
                display[row][col] = 1
        return display

    def rotate_col(self, shift, display):
        temp = []
        for row in range(0, len(display)):
            temp.append(display[row][shift[0]])
        temp = temp[-shift[1]:]+temp[:-shift[1]]
        for row in range(0, len(display)):
            display[row][shift[0]] = temp[row]
        return display

    def rotate_row(self, row, shift, display):
        display[row] = display[row][-shift:]+display[row][:-shift]
        return display

    def parse_input(self, data, display):
        for line in data.split("\n"):
            if "rect " in line:
                display = self.rect([int(s) for s in re.findall(r'\d+', line)], display)
            if "rotate row " in line:
                print(re.findall(r'\d+', line))
            if "rotate column " in line:
                display = self.rotate_col([int(s) for s in re.findall(r'\d+', line)], display)
        return display
