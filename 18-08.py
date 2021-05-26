
#cat > raw_socket.py

#Python 2.7
#-*-coding:utf-8 -*-
import socket, sys
from struct import *
try:
	#s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_RAW)
	s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP)
	s.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)
	s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
except socket.error, msg:
        print "Failed to create socket. Error code: " + str(msg[0]) + ", Error message : " + msg[1]
        sys.exit()

#IP Header
version = 4
header_length = 5
version_header_length = (version << 4) + header_length
tos = 0
total_length = 0 
id = 54321
fragment_offset = 0
ttl = 255
protocol = socket.IPPROTO_TCP
header_checksum = 0
ip_source = "127.0.0.1"
ip_destination = "127.0.0.1"
source_ip_address = socket.inet_aton(ip_source) 
destination_ip_address = socket.inet_aton(ip_destination)

ip_header = pack("!BBHHHBBH4s4s", version_header_length, tos, total_length, id, fragment_offset, ttl, protocol, header_checksum, source_ip_address, destination_ip_address)

#TCP Header
source_port = 12345
destination_port = 22
sequence_number = 123
acknowledgment_number = 0
offset = 5
reserved = 0
offset = (offset << 4) + reserved

#TCP flags
fin = 0
syn = 1
rst = 0
psh = 0
ack = 0
urg = 0
flags = (urg << 5) + (ack << 4) + (psh << 3) + (rst << 2) + (syn << 1) + (fin << 0)
window = socket.htons(5840)
checksum = 0
urgent_pointer = 0

tcp_header = pack("!HHLLBBHHH", source_port, destination_port, sequence_number, acknowledgment_number, offset, flags, window, checksum, urgent_pointer)

#Payload Data
payload_data = "Python Raw Socket"

#IP Packet
ip_packet = ip_header + tcp_header + payload_data

print s.sendto(ip_packet, (ip_destination, 0))

#python raw_socket.py
