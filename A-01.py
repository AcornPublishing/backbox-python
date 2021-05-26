
#cat > echo_server.py

#Python 2.7
#-*-coding:utf-8 -*-
import SocketServer

host = "127.0.0.1"
port = 9999

class MyTCPHandler(SocketServer.BaseRequestHandler):
	def handle(self):
		self.data = self.request.recv(65565).strip()
		print "{} wrote:".format(self.client_address[0])
		print self.data
		self.request.sendall(self.data.upper())

server = SocketServer.TCPServer((host, port), MyTCPHandler)

server.serve_forever()

#python echo_server.py &
