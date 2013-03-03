import socket
import World


class Server:
	"""Server."""

	def __init__(self, port):
		self.addr = ('', port)
		self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.s.setblocking(0)
		self.s.bind(self.addr)
		self.connections = []

		self.world = World.World(8, 8)
		self.chars = ["0", "1", "2", "3", "4", "5", "6", "7"]

	def __del__(self):
		for conn in self.connections:
			conn.close()
			"Closed connection (server stop)"

	def serve(self):
		running = True
		while running:
			try:
				try:
					self.s.listen(1)
					conn = self.s.accept()
					self.connections.append(conn)
					print "Opened connection"
					char = self.chars[len(self.connections - 1)]
					self.init_client(conn, char)
				except socket.error:
					pass

				for conn in self.connections:
					conn_sock = conn[0]
					try:
						data = conn_sock.recv(1024)
						if len(data) == 0:
							conn_sock.close()
							self.connections.remove(conn)
							print "Closed connection (client d/c)"
						else:
							print data
					except:
						pass
			except KeyboardInterrupt:
				running = False
		for conn in self.connections:
			conn.close()
			"Closed connection (server stop)"

	def init_client(self, conn):
		conn_sock = conn[0]
		data = ",".join(["INIT", world.get_width(), world.get_height(), char])
		conn_sock.send(data)
