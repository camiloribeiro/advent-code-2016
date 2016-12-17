class Ip:

    def parse(self, ip):
        return [ip[0:4], ip[5:9], ip[10:14]]

    def check_abba(self, fragment):
        return fragment[0] == fragment[-1] and fragment[1] == fragment[2]

    def support_tls(self, ip):
        parsed_ip = self.parse(ip)
        return (self.check_abba(parsed_ip[0]) or self.check_abba(parsed_ip[2]) and not self.check_abba(parsed_ip[1]))
