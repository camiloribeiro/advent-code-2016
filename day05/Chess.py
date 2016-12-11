import md5


class Chess:

    def get_key_for_character(self, character):
        password, index = '', 0
        while len(password) != 8:
            m = md5.new(character + str(index))
            current = m.hexdigest()
            if current.startswith("00000"):
                password += current[5]
            index += 1
        return password
