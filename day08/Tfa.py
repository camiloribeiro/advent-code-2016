class Tfa:
    def lighted_elements(self):
        display, lighted = [[0 for x in range(50)] for y in range(8)], 0
        for row in range(len(display)):
            for col in range(len(display[0])):
                lighted += display[row][col]
        return lighted

    def react(self, h, w, display):
        for row in range(0, h):
            for col in range(0, w):
                display[row][col] = 1
        return display

    def rotate_col(self, col, shift, display):
        temp = []
        for row in range(0, len(display)):
            temp.append(display[row][col])
        temp = temp[-shift:]+temp[:-shift]
        for row in range(0, len(display)):
            display[row][col] = temp[row]
        return display

    def rotate_row(self, row, shift, display):
        display[row] = display[row][-shift:]+display[row][:-shift]
        return display
