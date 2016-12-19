from Ip import Ip


ip = Ip()
print(ip.count_tls_ips(open("day07/input.txt").read()))
print(ip.count_ssl_ips(open("day07/input.txt").read())) # 169 low
