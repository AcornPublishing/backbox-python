
#cat > arp_monitoring.py

#Python 2.7
#-*-coding:utf-8 -*-
from scapy.all import *

def arp_monitor_callback(pkt):
	if (ARP in pkt) and (pkt[ARP].op in (1, 2)):
		return pkt.sprintf("%ARP.hwsrc% %ARP.psrc%")

sniff(prn = arp_monitor_callback, filter = "arp", store = 0)

#python arp_monitoring.py
