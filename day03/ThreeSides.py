class ThreeSides:

    def is_a_valid_triangle(self, side_a, side_b, side_c):
        return ((side_a + side_b > side_c) and (side_b + side_c > side_a) and (side_c + side_a > side_b))
