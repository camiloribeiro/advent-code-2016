class Tfa:
    def lighted_elements(self):
        w, h = 50, 8
        display = [[0 for x in range(w)] for y in range(h)]
        total = 0
        for row in range(len(display)):
            for col in range(len(display[0])):
                total += display[row][col]
        return total

    def react(self, h, w, display):
        for row in range(0, h):
            for col in range(0, w):
                display[row][col] = 1
        return display
