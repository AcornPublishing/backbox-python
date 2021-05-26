
#cat > gethostbyname.py

#Python 2.7
#-*-coding:utf-8 -*-
import socket
import sys
host = "www.google.com"
port = 80
try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
except socket.error, msg:
        print "Failed to create socket. Error code: " + str(msg[0]) + ", Error message : " + msg[1]
        sys.exit()
try:
        remote_ip = socket.gethostbyname(host)
except socket.gaierror:
        print "Hostname could not be resolved. Exiting"
        sys.exit()
s.connect((remote_ip, port))
print "Socket Connected to " + host + " on IP " + remote_ip
s.close()

#python gethostbyname.py
