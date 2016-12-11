import md5


class Chess:

    def get_key_for_character(self, character):
        index = 0
        while True:
            m = md5.new(character + str(index))
            current = m.hexdigest()
            if current.startswith("00000"):
                return current[5]
            index += 1
