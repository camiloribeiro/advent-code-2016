class Ip:

    def parse(self, ip):
        return [ip[0:4], ip[5:9], ip[10:14]]
