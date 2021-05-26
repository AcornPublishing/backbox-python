
#cat > tcp_server.py

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
try:
        s.bind((host, port))
except socket.error, msg:
        print "Failed to bind socket. Error Code : " + str(msg[0]) + " Message : " + msg[1]
        sys.exit()
s.listen(10)
(connection, address) = s.accept()
print connection
print address
connection.send("Thank you for connecting!")
connection.close()
s.close()

#python tcp_server.py &
