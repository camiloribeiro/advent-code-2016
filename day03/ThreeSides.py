class ThreeSides:

    def is_a_valid_triangle(self, ts):
        return ((ts[0] + ts[1] > ts[2]) and (ts[1] + ts[2] > ts[0]) and (ts[2] + ts[0] > ts[1]))

    def get_valid_triangles(self, data):
        triangles = 0
        for candidate in data.strip().split("\n"):
            if self.is_a_valid_triangle(map(int, candidate.split())):
                triangles += 1
        return triangles
