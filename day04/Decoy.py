class Decoy:

    def parse_room(self, room):
        return room.replace(']', '').rsplit("[", 1)

    def check_checksum(self, room):
        elements, sector_id = room[0].rsplit("-", 1)
        valid_elements = [x for x in list(elements) if x not in list("0123456789-")]
        d = {i: valid_elements.count(i) for i in valid_elements}
        if ''.join([v[0] for v in sorted(d.iteritems(), key=lambda(k, v): (-v, k))][:5]) == room[1]:
            return [int(sector_id), elements]
        return [0]

    def get_total_sectors(self, data):
        total_sector = 0
        for room in data.split("\n"):
            total_sector += self.check_checksum(self.parse_room(room))[0]
        return total_sector

    def get_all_valid_rooms(self, data):
        rooms = []
        for room in data.split("\n"):
            rooms.append(self.check_checksum(self.parse_room(room)))
        return filter(lambda a: a != [0], rooms)

    def decode_room(self, data):
        name = []
        room, sector = data.rsplit("-", 1)
        for letter in list(room.replace("-", " ")):
            current = (ord(letter)) + (int(sector) % 26)
            if current > 122:
                current = current - 26
            name.append(chr(current))
        return ''.join(name).replace('%', ' ')
