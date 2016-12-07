class Decoy:

    def parse_room(self, room):
        return room.replace(']', '').rsplit("[", 1)
