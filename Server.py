import socket
import World


class Server:
	"""Server."""

	def __init__(self, port):
		self.addr = ('', port)
		self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.s.settimeout(1.0)
		self.s.bind(self.addr)
		self.connections = []

		self.world = World.World(8, 8)
		self.chars = ["0", "1", "2", "3", "4", "5", "6", "7"]

	def __del__(self):
		for conn in self.connections:
			conn_sock = conn[0]
			conn_sock.close()
		print "Closed all connections (server stop)."

	def serve(self):
		running = True
		while running:
			try:
				try:
					self.s.listen(1)
					conn = self.s.accept()
					self.connections.append(conn)
					print "Opened connection. Now at " + str(len(self.connections)) + " connections."
					char = self.chars[len(self.connections) - 1]
					self.init_client(conn, char)
					self.update_client(conn)
				except socket.timeout:
					pass

				for conn in self.connections:
					conn_sock = conn[0]
					try:
						data = conn_sock.recv(1024)
						if len(data) == 0:
							conn_sock.close()
							self.connections.remove(conn)
							print "Closed connection (client d/c). Now at " + str(len(self.connections)) + " connections."
						else:
							print data
					except:
						pass
			except KeyboardInterrupt:
				running = False
		del(self)

	def init_client(self, conn, char):
		conn_sock = conn[0]
		data = ["INIT"]
		width_height = self.world.get_width_height()
		data += [str(width_height[0]), str(width_height[1]), char]
		message = ",".join(data)
		conn_sock.send(message + ";")

	def update_client(self, conn):
		conn_sock = conn[0]
		data = ["WORLD"]
		data += self.world.get_list()
		message = ",".join(data)
		conn_sock.send(message + ";")
