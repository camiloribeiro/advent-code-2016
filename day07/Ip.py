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
            if (ip[i] == ip[i + 3] and ip[i + 1] == ip[i + 2] and ip[i + 0] != ip[i + 1]):
                return True
        return False

    def support_tls(self, ip):
        ips = self.parse(ip,  [], [])
        return (any(self.check_abba(ip) for ip in ips[0])) and not (any(self.check_abba(ip) for ip in ips[1]))

    def count_tls_ips(self, ips):
        tls_count = 0
        for ip in ips.split("\n"):
            if self.support_tls(ip):
                tls_count += 1
        return tls_count
