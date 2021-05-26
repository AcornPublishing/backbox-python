
#cat > echo_client.py

#Python 2.7
#-*-coding:utf-8 -*-
import sys
import socket

host = "127.0.0.1"
port = 9999

data = " ".join(sys.argv[1:])
print "data = %s" %data

try:
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP)
	s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
except socket.error, msg:
        print "Failed to create socket. Error Code : " + str(msg[0]) + " Message : " + msg[1]
        sys.exit()
try:
	s.connect((host, port))
	s.sendall(bytes(data + "\n"))
	received = str(s.recv(65565))
finally:
	s.close()

print("Sent:     {}".format(data))
print("Received: {}".format(received))

#python echo_client.py Hello, Python!
