
#cat > raw_socket.py

#Python 2.7
#-*-coding:utf-8 -*-
import socket
from struct import *

def ethernet_addr(p):
	form = "%.2x:%.2x:%.2x:%.2x:%.2x:%.2x" %(ord(p[0]), ord(p[1]), ord(p[2]), ord(p[3]), ord(p[4]), ord(p[5]))
	return form
 
s = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(0x0003))

data = s.recvfrom(65565)

data = data[0]

ethernet_header_length = 14
EH = data[:ethernet_header_length]
ethernet_header = unpack("!6s6sH", EH)
ethernet_type = socket.ntohs(ethernet_header[2])

print "Desination MAC Address:", ethernet_addr(data[0:6])
print "Source MAC Address:", ethernet_addr(data[6:12])
print "Type:", str(ethernet_type)
print

if ethernet_type == 8:
	IH = data[ethernet_header_length:ethernet_header_length + 20]
        ip_header = unpack("!BBHHHBBH4s4s", IH)
 
        version_ip_header_length = ip_header[0]
        version = version_ip_header_length >> 4
        ip_header_length = version_ip_header_length & 0xF
        ip_header_length = ip_header_length * 4
        ttl = ip_header[5]
        protocol = ip_header[6]
        ip_source_address = socket.inet_ntoa(ip_header[8])
        ip_destination_address = socket.inet_ntoa(ip_header[9])
	 
        print "Version:", str(version)
	print "IP Header Length:", str(ip_header_length)
	print "TTL:", str(ttl)
	print "Protocol:", str(protocol)
	print "Source IP Address:", str(ip_source_address)
	print "Destination IP Address:", str(ip_destination_address)
	print

	if protocol == 6:
		length = ip_header_length + ethernet_header_length
		TH = data[length:length + 20]
		tcp_header = unpack("!HHLLBBHHH", TH)
             
		source_port = tcp_header[0]
		destination_port = tcp_header[1]
		sequence_number = tcp_header[2]
		acknowledgment_number = tcp_header[3]
		offset_reserved = tcp_header[4]
		tcp_header_length = offset_reserved >> 4
             
		print "Source Port:", str(source_port)
		print "Dest Port:", str(destination_port)
		print "Sequence Number:", str(sequence_number)
		print "Acknowledgment Number:", str(acknowledgment_number)
		print "TCP header length:", str(tcp_header_length)
		print

		header_size = ethernet_header_length + ip_header_length + (tcp_header_length * 4)
		payload_data_size = len(data) - header_size

		payload_data = data[header_size:]
             
		print "payload_data : " + payload_data
		print

	elif protocol == 1:
		length = ip_header_length + ethernet_header_length
		icmp_header_length = 8
		IH = data[length:length + 8]
		icmp_header = unpack("!BBH", IH)
             
		icmp_type = icmp_header[0]
		code = icmp_header[1]
		checksum = icmp_header[2]
             
		print "Type:", str(icmp_type)
		print "Code:", str(code)
		print "Checksum:", str(checksum)
		print

		header_size = ethernet_header_length + ip_header_length + icmp_header_length
		payload_data_size = len(data) - header_size

		payload_data = data[header_size:]
          
		print "payload_data : " + payload_data
		print

	elif protocol == 17:
		length = ip_header_length + ethernet_header_length
		udp_header_length = 8
		UH = data[length:length + 8]
		udp_header = unpack("!HHHH", UH)
             
		source_port = udp_header[0]
		destination_port = udp_header[1]
		length = udp_header[2]
		checksum = udp_header[3]
             
		print "Source Port:", str(source_port)
		print "Dest Port:", str(destination_port)
		print "Length:", str(length)
		print "Checksum:", str(checksum)
		print

		header_size = ethernet_header_length + ip_header_length + udp_header_length
		payload_data_size = len(data) - header_size

		payload_data = data[header_size:]
             
		print "payload_data : " + payload_data
		print

	else:
		print "Protocol other than TCP/UDP/ICMP"
 		print

#python raw_socket.py
