import ipaddress
import optparse
import random

class IPer():
    def __init__(self, ip_range):
        self.ip_range = ipaddress.IPv4Network('192.168.0.0/24')
    
    def get_ips(netrange):
        hosts = list(ipaddress.ip_network(netrange).hosts())
        thirty_percent = len(hosts)*.3
        the_choosen = random.choices(hosts,k=int(thirty_percent))
        return the_choosen

def main():
    parser = optparse.OptionParser()
    parser.add_option("-q", "--query", dest='range',
            help="enter your network range(s)") 

    (options,args) = parser.parse_args()

    if options.range == None:
        print(parser.usage)
        exit(0)
    else:
        the_range = options.range

    ipaddresses = IPer.get_ips(the_range)
    for ip in ipaddresses:
        print(ip)
        

        

if __name__ == "__main__":
    main()
