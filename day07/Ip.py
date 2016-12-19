class Ip:

    def parse(self, ip, out, ins):
        if "[" not in ip:
            ins.append(ip),
            return [ins, out]
        else:
            ins.append(ip[ip.find(""):ip.find("[")])
            out.append(ip[ip.find("[")+1:ip.find("]")])
            return self.parse(ip.split(']', 1)[-1], out, ins)

    def check_abba(self, ip):
        for i in range(0, len(ip) - 3):
            if (ip[i] == ip[i + 3] and ip[i + 1] == ip[i + 2] and ip[i] != ip[i + 1]):
                return True
        return False
    
    def support_tls(self, ip):
        ips = self.parse(ip,  [], [])
        return (any(self.check_abba(ip) for ip in ips[0])) and not (any(self.check_abba(ip) for ip in ips[1]))

    def check_aba(self, ips):
        abas = []
        for ip in ips:
            for i in range(0, len(ip) - 2):
                if (ip[i] == ip[i + 2] and ip[i] != ip[i + 1]):
                    abas.append(ip[i:i + 3])
        return abas

    def check_bab(self, ips, abas):
        for aba in abas:
            a, b = aba[0], aba[1]
            for ip in ips:
                for i in range(0, len(ip) - 2):
                    if (ip[i] == b and ip[i + 1] == a and ip[i + 2] == b):
                        return True
        return False

    def support_ssl(self, ips):
        ip_segments = self.parse(ips,  [], [])
        abas = []
        abas = self.check_aba(ip_segments[0])
        if not abas:
            return False
        abas = filter(lambda a: a != [], abas)
        if self.check_bab(ip_segments[1], abas):
            return True
        return False

    def count_tls_ips(self, ips):
        tls_count = 0
        for ip in ips.split("\n"):
            if self.support_tls(ip):
                tls_count += 1
        return tls_count

    def count_ssl_ips(self, ips):
        ssl_count = 0
        for ip in ips.split("\n"):
            if self.support_ssl(ip):
                ssl_count += 1
        return ssl_count
