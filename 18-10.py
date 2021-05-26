
#cat > raw_socket.py

#Python 2.7
#-*-coding:utf-8 -*-
import socket
from struct import *

s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP)
s.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

data = s.recv(65565)

ip_header = data[0:20]
new_ip_header = unpack("!BBHHHBBH4s4s", ip_header)
     
version_ip_header_length = new_ip_header[0]
version = version_ip_header_length >> 4
ip_header_length = version_ip_header_length & 0xF
new_ip_header_length = ip_header_length * 4
ip_ttl = new_ip_header[5]
ip_protocol = new_ip_header[6]
ip_source_address = socket.inet_ntoa(new_ip_header[8])
ip_destination_address = socket.inet_ntoa(new_ip_header[9])

print "Version:", str(version)
print "IP Header Length:", str(ip_header_length)
print "TTL:", str(ip_ttl)
print "Protocol:", str(ip_protocol)
print "Source IP Address:", str(ip_source_address)
print "Destination IP Address:", str(ip_destination_address)
print
     
tcp_header = data[new_ip_header_length:new_ip_header_length + 20]
new_tcp_header = unpack("!HHLLBBHHH", tcp_header)
     
tcp_source_port = new_tcp_header[0]
tcp_destination_port = new_tcp_header[1]
tcp_sequence_number = new_tcp_header[2]
tcp_acknowledgment_number = new_tcp_header[3]
tcp_offset_reserved = new_tcp_header[4]
new_tcp_header_length = tcp_offset_reserved >> 4
     
print "Source Port Number:", str(tcp_source_port)
print "Destination Port Number:", str(tcp_destination_port)
print "Sequence Number:", str(tcp_sequence_number)
print "Acknowledgment Number:", str(tcp_acknowledgment_number)
print "Header Length:", str(new_tcp_header_length)
print

header_size = new_ip_header_length + (new_tcp_header_length * 4)
payload_data_size = len(data) - header_size
     
payload_data = data[header_size:]
     
print "Payload Data:" + payload_data
print

#python raw_socket.py
