class Ip:

    def parse(self, ip):
        return [ip.split("[")[0], ip.split("[")[-1].split("]")[0], ip.split("]")[-1]]

    def check_abba(self, ip):
        for i in range(0, len(ip) - 3):
            if (ip[i] == ip[i + 3] and ip[i + 1] == ip[i + 2] and ip[i + 0] != ip[i + 1]):
                return True
        return False

    def support_tls(self, ip):
        parsed_ip = self.parse(ip)
        return (self.check_abba(parsed_ip[0]) or self.check_abba(parsed_ip[2]) and not self.check_abba(parsed_ip[1]))
