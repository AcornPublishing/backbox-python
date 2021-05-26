
#cat > tcp_client.py

#Python 2.7
#-*-coding:utf-8 -*-
import socket
import sys
host = "127.0.0.1"
port = 12345
try:
        #s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	#s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP)
	s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
except socket.error, msg:
        print "Failed to create socket. Error Code : " + str(msg[0]) + " Message : " + msg[1]
        sys.exit()
s.connect((host, port))
data = s.recv(65565)
print "Recevied Data:", data
s.close()

#python tcp_client.py
