from scapy.all import *
from scapy.layers.dns import DNS, DNSQR
from scapy.layers.inet import IP, UDP

# Set up the IP and DNS layers
ip = IP(dst="8.8.8.8")
udp = UDP(dport=53)
dns = DNS(rd=1, qd=DNSQR(qname="google.com"))

# Combine the layers and send the packet
packet = ip / udp / dns
response = sr1(packet, verbose=0)

# Print the DNS response
print(response.summary())
