
#cat > telnet.py

#Python 2.7
#-*-coding:utf-8 -*-
import socket, select, string, sys

if __name__ == "__main__":
	if(len(sys.argv) < 3):
		print "Usage: python telnet.py hostname port"
		sys.exit()
	host = sys.argv[1]
	port = int(sys.argv[2])
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	try:
		s.connect((host, port))
	except:
		print "Unable to connect"
		sys.exit()
	while True:
		socket_list = [sys.stdin, s]
		(read_sockets, write_sockets, error_sockets) = select.select(socket_list, [], [])
		for sock in read_sockets:
			if sock == s:
				data = sock.recv(65565)
				if not data:
					print "Connection closed"
					sys.exit()
				else:
					sys.stdout.write(data)
			else:
				msg = sys.stdin.readline()
				s.send(msg)

#python telnet.py google.com 80 

#GET/HTTP/1.1
