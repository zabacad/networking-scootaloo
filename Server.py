import socket


class Server:
	"""Server."""

	def __init__(self, port):
		self.addr = ('', port)
		self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.s.setblocking(0)
		self.s.bind(self.addr)
		self.connections = []

		#self.world

		while True:
			try:
				self.s.listen(1)
				self.connections.append(self.s.accept())
				print "Got connection"
			except socket.error:
				pass

			for conn in self.connections:
				conn_sock = conn[0]
				try:
					data = conn_sock.recv(1024)
					print data
				except:
					pass

	def __del__(self):
		for conn in self.connections:
			conn.close()
			"Closed connection (server stop)"
