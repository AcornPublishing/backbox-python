
#cat > raw_socket.py

#Python 2.7
#-*-coding:utf-8 -*-
import socket
import struct
import binascii

try:
	s = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.htons(0x0800))
	s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
except socket.error, msg:
	print "Failed to create socket. Error Code : " + str(msg[0]) + " Message : " + msg[1]
	sys.exit()

data = s.recvfrom(65565)

print "Data:", data
print

#Ethernet Header
ethernet_header = data[0][0:14]
ethernet_header = struct.unpack("!6s6s2s", ethernet_header)

print "Desination MAC Address:", binascii.hexlify(ethernet_header[0])
print "Source MAC Address:", binascii.hexlify(ethernet_header[1])
print

#IP Header
ip_header = data[0][14:34]
ip_header = struct.unpack("!12s4s4s", ip_header)

print "Source IP:", socket.inet_ntoa(ip_header[1])
print "Destination IP:", socket.inet_ntoa(ip_header[2])
print

#TCP Header
tcp_header = data[0][34:54]
tcp_header = struct.unpack("!2H16s", tcp_header)

print "Source Port Number:", tcp_header[0]
print "Destination Port Number:", tcp_header[1]
print

#python raw_socket.py
