class Decoy:

    def parse_room(self, room):
        return room.replace(']', '').rsplit("[", 1)

    def check_checksum(self, room):
        elements, sector_id = room[0].rsplit("-", 1)
        valid_elements = [x for x in list(elements) if x not in list("0123456789-")]
        d = {i: valid_elements.count(i) for i in valid_elements}
        if ''.join([v[0] for v in sorted(d.iteritems(), key=lambda(k, v): (-v, k))][:5]) == room[1]:
            return int(sector_id)
        return False
