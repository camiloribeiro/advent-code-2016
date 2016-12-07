class ThreeSides:

    def is_a_valid_triangle(self, ts):
        return ((ts[0] + ts[1] > ts[2]) and (ts[1] + ts[2] > ts[0]) and (ts[2] + ts[0] > ts[1]))

    def get_valid_triangles(self, data):
        triangles = 0
        for candidate in data.strip().split("\n"):
            if self.is_a_valid_triangle(map(int, candidate.split())):
                triangles += 1
        return triangles

    def get_valid_triangles_by_column(self, data):
        triangles, c1, c2, c3 = 0, [], [], []
        for line in data.strip().split("\n"):
            x, y, z = line.strip().split()
            c1.append(int(x))
            c2.append(int(y))
            c3.append(int(z.strip()))
        dimensions = c1 + c2 + c3
        candidates = [dimensions[i:i + 3] for i in range(0, len(dimensions), 3)]
        for candidate in candidates:
            if self.is_a_valid_triangle(candidate):
                    triangles += 1
        return triangles
