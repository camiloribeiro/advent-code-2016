import md5


class Chess:

    def get_simple_password(self, character):
        password, index = '', 0
        while len(password) != 8:
            m = md5.new(character + str(index))
            current = m.hexdigest()
            if current.startswith("00000"):
                password += current[5]
            index += 1
        return password

    def get_enhanced_password(self, character):
        password, index = '        ', 0
        while ' ' in password:
            m = md5.new(character + str(index))
            current = m.hexdigest()
            if current.startswith("00000"):
                if current[5].isdigit() and int(current[5]) < 8:
                    p = list(password)
                    if p[int(current[5])] is ' ':
                        p[int(current[5])] = current[6]
                    password = "".join(p)
            index += 1
        return password
