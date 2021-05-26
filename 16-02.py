
#cat > udp_client.py

#Python 2.7
#-*-coding:utf-8 -*-
import socket
import sys
host = "127.0.0.1"
port = 12345
try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	#s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0)
	#s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
except socket.error, msg:
        print "Failed to create socket. Error Code : " + str(msg[0]) + " Message : " + msg[1]
        sys.exit()
print s.sendto("Hello World!", (host, port))
s.close()

#python udp_client.py
