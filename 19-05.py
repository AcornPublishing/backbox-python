
#cat > raw_socket.py

#Python 2.7
#-*-coding:utf-8 -*-
import socket
import struct
import binascii

try:
	s = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.htons(0x0806))
	s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
except socket.error, msg:
	print "Failed to create socket. Error Code : " + str(msg[0]) + " Message : " + msg[1]
	sys.exit()

while True:
	data = s.recvfrom(65565)

	print "Data:", data
	print

#Ethernet Header
	ethernet_header = data[0][0:14]
	ethernet_header = struct.unpack("!6s6s2s", ethernet_header)

	print "Desination MAC Address:", binascii.hexlify(ethernet_header[0])
	print "Source MAC Address:", binascii.hexlify(ethernet_header[1])
	print "Type:", binascii.hexlify(ethernet_header[2])
	print

#ARP Header
	arp_header = data[0][14:42]
	arp_header = struct.unpack("!2s2s1s1s2s6s4s6s4s", arp_header)

	print "Hardware Type:", binascii.hexlify(arp_header[0])
	print "Protocol Type:", binascii.hexlify(arp_header[1])
	print "Hardware Size:", binascii.hexlify(arp_header[2])
	print "Protocol Size:", binascii.hexlify(arp_header[3])
	print "OP Code:", binascii.hexlify(arp_header[4])
	print "Source MAC Address:", binascii.hexlify(arp_header[5])
	print "Source IP Address:", socket.inet_ntoa(arp_header[6])
	print "Desination MAC Address:", binascii.hexlify(arp_header[7])
	print "Destination IP Address:", socket.inet_ntoa(arp_header[8])
	print

#python raw_socket.py
